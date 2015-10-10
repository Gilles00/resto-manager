$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

$(function() {
	var successDiv = "<div class='alert alert-success'></div>";
	var infoDiv = "<div class='alert alert-info'></div>";
	var errorDiv = "<div class='alert alert-danger'></div>";
	
	$("li.success").wrap(successDiv);
	$("li.info").wrap(infoDiv);
	$("li.error").wrap(errorDiv);
	
	$("#btn_visite_guidee").click(function() {
		startClientTour();
	});
	
	$(document).on("blur", ".repas_qty", function(event) {
		var total = 0;
		
		restaurantId = event.target.getAttribute('data-restaurant');
		repasId = event.target.getAttribute('data-id');
		
		$("#price_" + repasId).html(($(event.target).attr("data-price") * $(event.target).val()).toFixed(2));
		
		$(".repas_qty[data-restaurant='" + restaurantId + "']").each(function() {
			total += $(this).attr("data-price") * $(this).val();
		});
		
		$("#lblTotal_" + restaurantId).html("$" + total.toFixed(2));
	});
	
	$(document).on("click", ".btn-confirm-commande", function(event) {
		// On met à jour le modal dialog pour le nouveau restaurateur à modifier
		// et on utilise getAttribute pour compatibilité sur les browsers un peu plus anciens
		var restaurantId = event.target.getAttribute('data-restaurant');

		var viewUrl = '/commandes/get_confirm_commande_message/' + restaurantId;
		
		$("#btnConfirmerCommande")[0].setAttribute('data-restaurant', restaurantId)
		
		$("#divConfirmerCommande").html("<img src='/static/images/ajax-loader.gif' alt='loading...' />");
		
		
		
		var restaurantId = event.target.getAttribute('data-restaurant');
		
		var viewUrl = '/commandes/get_confirm_commande_message/' + restaurantId;
		
		var options = {
			url: viewUrl,
			type: 'post',
			target: '#divConfirmerCommande',
			success: function() {
				$('.timepicker').timepicker({
					hours: { starts: 10, ends: 22 }});
				$('.datepicker').datepicker({minDate: 0});
			}
		};
		
		$("#sidebar-form-restaurant-" + restaurantId).ajaxSubmit(options);
	});
	
	$(document).on("click", "#btnConfirmerCommande", function(event) {
		var restaurantId = event.target.getAttribute('data-restaurant');
		
		var viewUrl = '/commandes/confirm_commande/' + restaurantId;
		
		var options = {
			url: viewUrl,
			type: 'post',
			success: function(data) {
				data = $.parseJSON(data);
				
				if (data.success == true) {
					restaurantId = data.restaurantId;
					commandeId = data.commandeId;
					
					$("#target-restaurant-" + restaurantId).remove();
					
					showCommandeNotification(commandeId);
				}
			}
		};
		
		$("#commandeFormConfirm").ajaxSubmit(options);
		
		return false;
	});
	
	$(".repas_qty").blur();
});


function showCommandeNotification(commandeId) {
	hideNotifications();

	$("#divNotificationsCommande").notify('Vous pouvez visualiser votre commande dans l\'onglet "Mes commandes".', {
		position: 'top center',
		clickToHide: false,
		autoHide: false,
		arrowSize: 0,
		style: 'bootstrap',
		className: 'success',
		showAnimation: 'fadeIn',
		hideAnimation: 'fadeOut'
	});
	
	$(".notifyjs-bootstrap-success").append("<br /><span>Voici votre numéro de confirmation: " + commandeId + "</span>");
}

function hideNotifications() {
	$(".notifyjs-bootstrap-info").trigger('notify-hide');
	$(".notifyjs-bootstrap-warn").trigger('notify-hide');
}


function isNumber(event) {
  if (event) {
    var charCode = (event.which) ? event.which : event.keyCode;
    if (charCode != 190 && charCode > 31 && 
       (charCode < 48 || charCode > 57) && 
       (charCode < 96 || charCode > 105) && 
       (charCode < 37 || charCode > 40) && 
        charCode != 110 && charCode != 8 && charCode != 46 )
       return false;
  }
  return true;
}

function startClientTour() {
	$(".popover.bottom").remove();

	var steps = [];
	
	// Fonctionne avec tourist.js
	if ($("#gerer_compte").length) {
		steps.push({
		  content: '<p>Cliquez ici pour modifier vos informations personnelles.</p>',
		  highlightTarget: true,
		  nextButton: true,
		  target: $('#gerer_compte'),
		  my: 'top center',
		  at: 'bottom center'
		});
	}
	
	if ($("#passer_commande").length) {
		steps.push({
		  content: '<p>Cliquez ici pour commander à partir de menus de restaurants.</p>',
		  highlightTarget: true,
		  nextButton: true,
		  target: $('#passer_commande'),
		  my: 'top center',
		  at: 'bottom center'
		});
	}
	
	if ($("#mes_commandes").length) {
		steps.push({
		  content: '<p>Cliquez ici pour visualiser les commandes que vous avez passées.</p>',
		  highlightTarget: true,
		  nextButton: true,
		  target: $('#mes_commandes'),
		  my: 'top center',
		  at: 'bottom center'
		});
	}
	
	if ($("#self_manage_restaurants").length) {
		steps.push({
		  content: '<p>Cliquez ici pour gérer les restaurants que vous possédez.</p>',
		  highlightTarget: true,
		  nextButton: true,
		  target: $('#self_manage_restaurants'),
		  my: 'top center',
		  at: 'bottom center'
		});
	}
	
	if ($("#gerer_restaurants").length) {
		steps.push({
		  content: '<p>Cliquez ici pour ajouter, modifier ou supprimer des restaurants. Vous pouvez également associer des restaurants à des restaurateurs.</p>',
		  highlightTarget: true,
		  nextButton: true,
		  target: $('#gerer_restaurants'),
		  my: 'top center',
		  at: 'bottom center'
		});
	}
	
	if ($("#gerer_restaurateurs").length) {
		steps.push({
		  content: '<p>Cliquez ici pour ajouter, modifier ou supprimer des restaurateurs. Vous pouvez également associer des restaurateurs à des restaurants.</p>',
		  highlightTarget: true,
		  nextButton: true,
		  target: $('#gerer_restaurateurs'),
		  my: 'top center',
		  at: 'bottom center'
		});
	}
	
	if ($("#deconnecter").length) {
		steps.push({
		  content: '<p>Lorsque vous avez terminé, cliquez ici pour fermer votre session.</p>',
		  highlightTarget: true,
		  nextButton: true,
		  target: $('#deconnecter'),
		  my: 'top center',
		  at: 'bottom center'
		});
	}

	var tour = new Tourist.Tour({
	  steps: steps,
	  tipClass: 'Bootstrap',
	  tipOptions:{ showEffect: 'slidein' }
	});

	tour.start();
}