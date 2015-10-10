$(function() {
	setUpAccordion();
	  
	$(document).on("click", ".add-to-commande", function(event) {
		var restaurantId = event.target.getAttribute('data-id');
		
		var viewUrl = '/commandes/add_repas/' + restaurantId;
		
		if (!$("#target-restaurant-" + restaurantId).length) {
			$("#target-commandes").append("<div id='target-restaurant-" + restaurantId + "'></div>");
		}
		
		var options = {
			url: viewUrl,
			type: 'post',
			success: function(data) {
				data = $.parseJSON(data);
				
				if (data.success == true) {
					restaurantId = data.restaurantId;
				
					appendToSidebar(restaurantId);
				}
			}
		};
		
		$("#commande-form-" + restaurantId).ajaxSubmit(options);
		
		return false;
	});
});
  
 function setUpAccordion() {
	$( "#accordion" )
		.accordion({
			header: "> div > h3",
			collapsible: true
	});
	  
	$('#accordion').hide();

	$('#accordion h3').first().click();

	window.setTimeout(showAccordion,400);
 }
  
 function showAccordion() {
	$('#accordion').show();
 }
 
 function appendToSidebar(restaurantId) {
	
	var viewUrl = "/commandes/get/" + restaurantId;

	$.get(viewUrl, function(data) {
		$("#target-restaurant-" + restaurantId).html(data);
	});
 }