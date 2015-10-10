$(function() {
	$(document).on("click", ".show_commandes", function(event) {
		var restaurantId = event.target.getAttribute('data-id');

		var viewUrl = '/commandes/get_commandes_by_restaurant/' + restaurantId;
		
		$("#divCommandesRestaurant").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
		$("#divCommandesRestaurant").load(viewUrl);
	});
	
	$(document).on("click", ".btnPreparerCommande", function(event) {
		var commandeId = event.target.getAttribute('data-commande_id');
		
		var viewUrl = '/commandes/preparer_commande/' + commandeId;

		$.post(viewUrl, function(data) {
			if (data == "success") {
				var btnTerminerCommande = "<a data-commande_id='" + commandeId + "' id='btnTerminerCommande" + commandeId + "' class='btnTerminerCommande btn btn-xs btn-success'>Terminer</a>"
				$("#btnPreparerCommande" + commandeId).replaceWith(btnTerminerCommande);
				
				$("#cellState" + commandeId).html("En préparation");
			}
		});
	});
	
	$(document).on("click", ".btnTerminerCommande", function(event) {
		var commandeId = event.target.getAttribute('data-commande_id');
		
		var viewUrl = '/commandes/terminer_commande/' + commandeId;

		$.post(viewUrl, function(data) {
			if (data == "success") {
				$("#btnTerminerCommande" + commandeId).remove()
				
				$("#cellState" + commandeId).html("Prête");
			}
		});
	});
});