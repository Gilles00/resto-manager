$(function() {
	$("#btnAjoutRestaurant").click(function() {
		$("#divAjoutRestaurant").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
		$("#divAjoutRestaurant").load("/restaurants/add");
	});
	
	$("#btnSaveRestaurant").click(function() {
		var options = {
			url: '/restaurants/add',
			type: 'post',
			target: '#divAjoutRestaurant',
			success: function(data) {
				$("#btnSaveRestaurant").button('reset'); // On réactive le bouton
				data = $.parseJSON(data);
				
				if (data.success == true) {
					$('#modalAjoutRestaurant').modal('hide');
					insertRestaurantRow(data.id);
					hideNotifications();
					
					if (data.noRestaurateur == true) {
						showNoRestaurateurNotification();
					}
				}
			}
		};
		
		$("#divAjoutRestaurant > form").ajaxSubmit(options);

        $("#btnSaveRestaurant").button('loading'); // On désactive  le bouton
		
		//$("#divAjoutRestaurant").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
	});
	
	$(document).on("click", "#undo_deletions", function() {
		var viewUrl = '/restaurants/undo_last_delete';
		
		$.post(viewUrl, function(data) {
			data = $.parseJSON(data);
		
			if (data.success == true) {
				insertRestaurantRow(data.id);
				hideNotifications();
			}
		});
	});
	
	$(document).on("click", ".delete-restaurant", function(event) {
		// On met à jour le modal dialog pour le nouveau restaurant à supprimer
		// et on utilise getAttribute pour compatibilité sur les browsers un peu plus anciens
		var restaurantId = event.target.getAttribute('data-id');
		
		$("#btnDeleteRestaurant")[0].setAttribute('data-id', restaurantId)
	});
	
	$("#btnDeleteRestaurant").click(function(event) {
		var restaurantId = event.target.getAttribute('data-id');
		event.target.setAttribute('data-id', '-1');
		
		if (restaurantId != -1) {
			var viewUrl = '/restaurants/delete/' + restaurantId;
		
			$.post(viewUrl, function(data) {
				if (data == "success") {
					$('#modalSuppressionRestaurant').modal('hide');
					$("#restaurant_" + restaurantId).remove();
					
					showDeletionNotification();
				}
			});
		}
	});
	
	$(document).on("click", ".edit-restaurant", function(event) {
		// On met à jour le modal dialog pour le nouveau restaurant à modifier
		// et on utilise getAttribute pour compatibilité sur les browsers un peu plus anciens
		var restaurantId = event.target.getAttribute('data-id');

		var viewUrl = '/restaurants/edit/' + restaurantId;
		
		$("#btnSaveEditRestaurant")[0].setAttribute('data-id', restaurantId)
		
		$("#divEditRestaurant").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
		$("#divEditRestaurant").load(viewUrl);
	});
	
	$("#btnSaveEditRestaurant").click(function(event) {
		var restaurantId = event.target.getAttribute('data-id');
		
		var viewUrl = '/restaurants/edit/' + restaurantId;
		
		var options = {
			url: viewUrl,
			type: 'post',
			target: '#divEditRestaurant',
			success: function(data) {
				$("#btnSaveEditRestaurant").button('reset'); // On réactive le bouton
				data = $.parseJSON(data);
				
				if (data.success == true) {
					$('#modalModificationRestaurant').modal('hide');
					editRestaurantRow(data.id);
					hideNotifications();
					
					if (data.noRestaurateur == true) {
						showNoRestaurateurNotification();
					}
				}
			}
		};
		
		$("#divEditRestaurant > form").ajaxSubmit(options);
		
		$("#btnSaveEditRestaurant").button('loading'); // On désactive  le bouton
		
		//$("#divEditRestaurant").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
	});
});

function insertRestaurantRow(restaurantId) {
	var viewUrl = "/restaurants/get/" + restaurantId;

	$.get(viewUrl, function(data) {
		$("#tblRestaurants tbody").append(data);
	});
}

function editRestaurantRow(restaurantId) {
	var viewUrl = "/restaurants/get/" + restaurantId;

	$.get(viewUrl, function(data) {
		$("#restaurant_" + restaurantId).replaceWith(data);
	});
}

function showDeletionNotification() {
	hideNotifications
	$("#undo_deletions").remove();

	$("#divNotifications").notify('Vous avez supprimé un restaurant. ', {
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

function showNoRestaurateurNotification() {
	hideNotifications();
	$("#undo_deletions").remove();

	$("#divNotifications").notify('Attention: Aucun restaurateur n\'a été assigné au restaurant. ', {
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