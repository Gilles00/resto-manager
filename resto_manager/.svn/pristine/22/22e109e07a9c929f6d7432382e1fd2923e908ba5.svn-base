

var markerArray = [];	
var waypoint = [];	// array contenant le waypoint du restaurant choisi

var restaurantChoisi = "beauharnois";  // les coordonnées resto choisi par le livreur
var ets;	// coor de l'éts pour centrer la carte
var startName;	// coor de départ
var endName;	// coor d'arrivée

var startLocation;
var endLocation;
var markerResto;
var stepDisplay;	// array contenant les infos a afficher pour un marqueur 'step'
var infowindow;
var directionsDisplay;
var directionsService;
var mapOptions;	// les options liés a la carte
var request;	// la requete qui pars vers google et affiche les infos
var imageMarkerResto;
var map; // la map utilisée 

//waypoint pour aller chercher la commande : mieux de faire a la fin quand le choix de commande sera réalisé



function initialize() {
	
	var ets = new google.maps.LatLng(45.4953573,-73.5630168);
  
	imageMarkerResto = "/static/images/restaurant.png";

	mapOptions = { zoom:12, center:ets};

	map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);

	directionsService = new google.maps.DirectionsService();
	directionsDisplay = new google.maps.DirectionsRenderer();

	directionsDisplay.setMap(map);
	directionsDisplay.setPanel(document.getElementById('directions-panel'));

	var control = document.getElementById('control');
	control.style.display = 'block';
	map.controls[google.maps.ControlPosition.TOP_CENTER].push(control);

	// Instantiate an info window to hold step text.
	stepDisplay = new google.maps.InfoWindow();

	var places = getArrayPlacesSmall();

	setRestoMarker(places);
	
}



function calcRoute(request) {
	// First, remove any existing markers from the map.
	for (var i = 0; i < markerArray.length; i++) {
		markerArray[i].setMap(null);
	}
	// Now, clear the array itself.
	markerArray = [];

	directionsService.route(request, function(response, status) {
		if (status == google.maps.DirectionsStatus.OK) {
			var warnings = document.getElementById('warnings_panel');
			warnings.innerHTML = '<b>' + response.routes[0].warnings + '</b>';

			directionsDisplay.setDirections(response);
			showSteps(response);
		}
	});
}


function showSteps(directionResult) {
	var myRoute = directionResult.routes[0].legs[0];

	for (var i = 0; i < myRoute.steps.length; i++) {
		var marker = new google.maps.Marker({
			position : myRoute.steps[i].start_location,
			map : map
		});
		attachInstructionText(marker, myRoute.steps[i].instructions);
		markerArray[i] = marker;
	}
}


function attachInstructionText(marker, text) {
	google.maps.event.addListener(marker, 'click', function() {
		// Open an info window when the marker is clicked on,
		// containing the text of the step.
		stepDisplay.setContent(text);
		stepDisplay.open(map, marker);
	});
}


function getArrayPlaces(){
	// ici on recevra les infos necessaires
	var places = [// [nom. adresse, telephone, latitude(pour maps), longitude(pour maps), nombre de commandes]
	              ['ets', 'ETS, Montreal, QC', '450-985-4871', 45.4953573, -73.5630168, 5],
	              ['1000 Rue de la Gauchetière', '1000 Rue de la Gauchetière, Montreal, QC, ', '584-965-8745', 45.498334, -73.566265, 6],
	              ['Station Angrignon', 'Station Angrignon Montreal, QC', '541-985-3214', 45.446294, -73.603752, 8],
	              ['Station Bonaventure', 'Station Bonaventure Montreal, QC', '450-934-4961', 45.498046, -73.566892, 2]
	              ];
	return places;
}



function getArrayPlacesSmall(){
	// ici on recevra les infos necessaires
	var places = [// [nom. adresse, telephone, latitude(pour maps), longitude(pour maps), nombre de commandes]
	              ['ets', 'ETS, Montreal, QC', '450-985-4871', 5],
	              ['1000 Rue de la Gauchetière', '1000 Rue de la Gauchetière, Montreal, QC, ', '584-965-8745', 6],
	              ['Station Angrignon', 'Station Angrignon Montreal, QC', '541-985-3214', 8],
	              ['Station Bonaventure', 'Station Bonaventure Montreal, QC', '450-934-4961', 2]
	              ];
	return places;
}



function setRestoMarker(places){
	
	var nbPlaces = places.length;
//	[nom. adresse, telephone, latitude(pour maps), longitude(pour maps), nombre de commandes]
	var geoCodedMarker;
	var geocoder = new google.maps.Geocoder();
	
	for (i = 0; i < nbPlaces; i++){
		
		var title = places[i][0];
		var contentString = '<div id="content">'+
		'</div>'+
		'<h1 id="firstHeading" class="firstHeading">'+title+'</h1>'+
		'<div id="bodyContent">'+
		'<p><b>Adresse: </b>'+places[i][1]+
		'<br/><b>Téléphone: </b>'+places[i][2]+
		'<br/><b>Nombre de commandes prêtes: </b><a href="www.google.com">'+places[i][3]+'</a></p>'+
		'</div>';

		console.log(places[i][1]);

		
		geocoder.geocode({'address': places[i][1]}, function(title, contentString) {
			return (function(results, status) {
				if (status == google.maps.GeocoderStatus.OK) {
					
					console.log("abc");
					console.log(title);
					console.log(contentString);
				    console.log(results[0].geometry.location);
				    console.log(results[0].formatted_address);
				    
			    	var markerResto = new google.maps.Marker({
						position: results[0].geometry.location,
						map:map,
						title: title,
						icon: imageMarkerResto
					});
			    	
			    	addListener(markerResto, contentString);
				}
			});
		});
	}

}


function addListener(marker, contentString){
	// le listener est ajouté séparément car autrement il listen tout les elements et répond tjrs de la meme facon pour tous
	//onclick on efface les window et on re dessinne celle quon veu, ca prend moin d'espace dans l'écran
	google.maps.event.addListener(marker, 'click', function() {
		if (infowindow) {
			infowindow.close();
		}
		infowindow = new google.maps.InfoWindow({
			content: contentString
		});
		infowindow.open(map,marker);
	});
}


function buildRequest(){

	console.log("dans fct");
	
	startName = document.getElementById('start').value;
	endName = document.getElementById('end').value;
	waypointName = document.getElementById('waypoint').value;

	waypoint.push({
		location:waypointName,
		stopover:true
	});
	
	request = {
			origin : startName,
			destination : endName,
			waypoints: waypoint,
			optimizeWaypoints: true,
			travelMode : google.maps.TravelMode.DRIVING
	}; 

	calcRoute(request);
	
}


/*

function buildRequest(startPosition, endPosition){
	/*
	start = document.getElementById('start').value;
	end = document.getElementById('end').value;
	
	var startPosition = getGeoLocationFromName(start); 
	var endPosition = getGeoLocationFromName(end); 

	console.log("Start:" + startPosition);
	
	var start2 = new google.maps.LatLng(startPosition.k, startPosition.B);
	var end2 = new google.maps.LatLng(endPosition.k, endPosition.B);
*/

/*
	waypoint.push({
		location:restaurantChoisi,
		stopover:true
	});

	request = {
			origin : start2,
			destination : end2,
			waypoints: waypoint,
			optimizeWaypoints: true,
			travelMode : google.maps.TravelMode.DRIVING
	};

	return request;
}
*/


google.maps.event.addDomListener(window, 'load', initialize);
