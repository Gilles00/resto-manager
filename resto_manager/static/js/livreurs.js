$(function() {
	$("#btnAjoutLivreur").click(function() {
		$("#divAjoutLivreur").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
		$("#divAjoutLivreur").load("/livreurs/add");
	});
	
	$("#btnSaveLivreur").click(function() {	
		var options = {
			url: '/livreurs/add',
			type: 'post',
			target: '#divAjoutLivreur',
			success: function(data) {
				$("#btnSaveLivreur").button('reset'); // On réactive le bouton
				data = $.parseJSON(data);
				
				if (data.success == true) {
					$('#modalAjoutLivreur').modal('hide');
					insertLivreurRow(data.id);
					hideNotifications();
				}
			}
		};
		
		$("#divAjoutLivreur > form").ajaxSubmit(options);

		$("#btnSaveLivreur").button('loading'); // On désactive  le bouton
	});
	
	$(document).on("click", ".btnLivrerCommande", function() {
		var commandeId = event.target.getAttribute('data-commandeId');
		
		var viewUrl = '/commandes/livrer_commande/' + commandeId;
		
		$.post(viewUrl, function(data) {
			if (data.success == "success") {
				$("#cellState" + commandeId).html("Livré");
			}
		});
	});
	
	$(document).on("click", "#undo_deletions", function() {
		var viewUrl = '/livreurs/undo_last_delete';
		
		$.post(viewUrl, function(data) {
			data = $.parseJSON(data);
		
			if (data.success == true) {
				insertLivreurRow(data.id);
				hideNotifications();
			}
		});
	});
	
	$(document).on("click", ".delete-livreur", function(event) {
		var livreurId = event.target.getAttribute('data-id');
		
		$("#btnDeleteLivreur")[0].setAttribute('data-id', livreurId)
	});
	
	$("#btnDeleteLivreur").click(function(event) {
		var livreurId = event.target.getAttribute('data-id');
		
		var viewUrl = '/livreurs/delete/' + livreurId;
		
		$.post(viewUrl, function(data) {
			if (data == "success") {
				$('#modalSuppressionLivreur').modal('hide');
				$("#livreur_" + livreurId).remove();
				
				showDeletionNotification();
			}
		});
	});
	
	$(document).on("click", ".edit-livreur", function(event) {
		var livreurId = event.target.getAttribute('data-id');

		var viewUrl = '/livreurs/edit/' + livreurId;
		
		$("#btnSaveEditLivreur")[0].setAttribute('data-id', livreurId)
		
		$("#divEditLivreur").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
		$("#divEditLivreur").load(viewUrl);
	});
	
	$("#btnSaveEditLivreur").click(function(event) {
		var livreurId = event.target.getAttribute('data-id');
		
		var viewUrl = '/livreurs/edit/' + livreurId;
		
		var options = {
			url: viewUrl,
			type: 'post',
			target: '#divEditLivreur',
			success: function(data) {
				$("#btnSaveEditLivreur").button('reset'); // On réactive le bouton
				data = $.parseJSON(data);
				
				if (data.success == true) {
					$('#modalModificationLivreur').modal('hide');
					editLivreurRow(data.id);
					hideNotifications();
				}
			}
		};
		
		$("#divEditLivreur > form").ajaxSubmit(options);
		
		$("#btnSaveEditLivreur").button('loading'); // On désactive  le bouton
	});
});

function insertLivreurRow(livreurId) {
	var viewUrl = "/livreurs/get/" + livreurId;

	$.get(viewUrl, function(data) {
		$("#tblLivreurs tbody").append(data);
	});
}

function editLivreurRow(livreurId) {
	var viewUrl = "/livreurs/get/" + livreurId;

	$.get(viewUrl, function(data) {
		$("#livreur_" + livreurId).replaceWith(data);
	});
}

function showDeletionNotification() {
	hideNotifications();
	$("#undo_deletions").remove();

	$("#divNotifications").notify('Vous avez supprimé un livreur. ', {
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

function hideNotifications() {
	$(".notifyjs-bootstrap-info").trigger('notify-hide');
	$(".notifyjs-bootstrap-warn").trigger('notify-hide');
}