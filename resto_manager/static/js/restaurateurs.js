$(function() {
	$("#btnAjoutRestaurateur").click(function() {
		$("#divAjoutRestaurateur").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
		$("#divAjoutRestaurateur").load("/restaurateurs/add");
	});
	
	$(document).on("click", ".btnDeleteRestaurant", function(event) {
		var restaurandId = event.target.getAttribute('data-restaurant_id');
		var nomRestaurant = $("#nomRestaurant" + restaurandId).html();
		
		$("#currentRestaurant" + restaurandId).remove();
		
		var optionNewRestaurant = "<option value='" + restaurandId + "'>" + nomRestaurant + "</option>";
		
		$("#ddlNewRestaurant").append(optionNewRestaurant);
	});

	$(document).on("click", "#btnAddRestaurant", function(event) {
		if ($("#ddlNewRestaurant").val() == null) {
			return;
		}
	
		var restaurandId = $("#ddlNewRestaurant").val();
		var nomRestaurant = $("#ddlNewRestaurant").find(":selected").text();
		
		var newContent = "<div id='currentRestaurant" + restaurandId + "'>"
		+		"<span id='nomRestaurant" + restaurandId + "'>" + nomRestaurant + "</span> "
		+		"<a style='margin-bottom: 5px;' data-restaurant_id='" + restaurandId + "' class='btnDeleteRestaurant btn btn-xs btn-danger'>X</a>"
		+		"<input name='restaurants' type='hidden' value='" + restaurandId + "' />"
		+ "</div>";

		$("#divCurrentRestaurants").append(newContent);
		
		$("#ddlNewRestaurant").find(":selected").remove();
		
		
	});
	
	$("#btnSaveRestaurateur").click(function() {	
		var options = {
			url: '/restaurateurs/add',
			type: 'post',
			target: '#divAjoutRestaurateur',
			success: function(data) {
				$("#btnSaveRestaurateur").button('reset'); // On réactive le bouton
				data = $.parseJSON(data);
				
				if (data.success == true) {
					$('#modalAjoutRestaurateur').modal('hide');
					insertRestaurateurRow(data.id);
					hideNotifications();
					
					if (data.noRestaurant == true) {
						showNoRestaurantNotification();
					}
				}
			}
		};
		
		$("#divAjoutRestaurateur > form").ajaxSubmit(options);

		$("#btnSaveRestaurateur").button('loading'); // On désactive  le bouton
		
		//$("#divAjoutRestaurateur").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
	});
	
	$(document).on("click", "#undo_deletions", function() {
		var viewUrl = '/restaurateurs/undo_last_delete';
		
		$.post(viewUrl, function(data) {
			data = $.parseJSON(data);
		
			if (data.success == true) {
				insertRestaurateurRow(data.id);
				hideNotifications();
			}
		});
	});
	
	$(document).on("click", ".delete-restaurateur", function(event) {
		// On met à jour le modal dialog pour le nouveau restaurateur à supprimer
		// et on utilise getAttribute pour compatibilité sur les browsers un peu plus anciens
		var restaurateurId = event.target.getAttribute('data-id');
		
		$("#btnDeleteRestaurateur")[0].setAttribute('data-id', restaurateurId)
	});
	
	$("#btnDeleteRestaurateur").click(function(event) {
		var restaurateurId = event.target.getAttribute('data-id');
		
		var viewUrl = '/restaurateurs/delete/' + restaurateurId;
		
		$.post(viewUrl, function(data) {
			if (data == "success") {
				$('#modalSuppressionRestaurateur').modal('hide');
				$("#restaurateur_" + restaurateurId).remove();
				
				showDeletionNotification();
			}
		});
	});
	
	$(document).on("click", ".edit-restaurateur", function(event) {
		// On met à jour le modal dialog pour le nouveau restaurateur à modifier
		// et on utilise getAttribute pour compatibilité sur les browsers un peu plus anciens
		var restaurateurId = event.target.getAttribute('data-id');

		var viewUrl = '/restaurateurs/edit/' + restaurateurId;
		
		$("#btnSaveEditRestaurateur")[0].setAttribute('data-id', restaurateurId)
		
		$("#divEditRestaurateur").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
		$("#divEditRestaurateur").load(viewUrl);
	});
	
	$("#btnSaveEditRestaurateur").click(function(event) {
		var restaurateurId = event.target.getAttribute('data-id');
		
		var viewUrl = '/restaurateurs/edit/' + restaurateurId;
		
		var options = {
			url: viewUrl,
			type: 'post',
			target: '#divEditRestaurateur',
			success: function(data) {
				$("#btnSaveEditRestaurateur").button('reset'); // On réactive le bouton
				data = $.parseJSON(data);
				
				if (data.success == true) {
					$('#modalModificationRestaurateur').modal('hide');
					editRestaurateurRow(data.id);
					hideNotifications();
					
					if (data.noRestaurant == true) {
						showNoRestaurantNotification();
					}
				}
			}
		};
		
		$("#divEditRestaurateur > form").ajaxSubmit(options);
		
		$("#btnSaveEditRestaurateur").button('loading'); // On désactive  le bouton
		
		//$("#divEditRestaurateur").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
	});
});

function insertRestaurateurRow(restaurateurId) {
	var viewUrl = "/restaurateurs/get/" + restaurateurId;

	$.get(viewUrl, function(data) {
		$("#tblRestaurateurs tbody").append(data);
	});
}

function editRestaurateurRow(restaurateurId) {
	var viewUrl = "/restaurateurs/get/" + restaurateurId;

	$.get(viewUrl, function(data) {
		$("#restaurateur_" + restaurateurId).replaceWith(data);
	});
}

function showDeletionNotification() {
	hideNotifications();
	$("#undo_deletions").remove();

	$("#divNotifications").notify('Vous avez supprimé un restaurateur. ', {
		position: 'top center',
		clickToHide: false,
		autoHide: false,
		arrowSize: 0,
		style: 'bootstrap',
		className: 'info',
		showAnimation: 'fadeIn',
		hideAnimation: 'fadeOut'
	});
	
	var linkUndo = "<a style='color: black;' id='undo_deletions'>Annuler</a>";
	
	$(".notifyjs-bootstrap-info").append(linkUndo);
}

function showNoRestaurantNotification() {
	hideNotifications();
	$("#undo_deletions").remove();

	$("#divNotifications").notify('Attention: Aucun restaurant n\'a été assigné au restaurateur. ', {
		position: 'top center',
		clickToHide: false,
		autoHide: false,
		arrowSize: 0,
		style: 'bootstrap',
		className: 'warn',
		showAnimation: 'fadeIn',
		hideAnimation: 'fadeOut'
	});
}

function hideNotifications() {
	$(".notifyjs-bootstrap-info").trigger('notify-hide');
	$(".notifyjs-bootstrap-warn").trigger('notify-hide');
}