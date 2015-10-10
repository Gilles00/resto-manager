var restoMarkerArray = [];
var markerArray = [];	
var waypoint = [];	// array contenant le waypoint du restaurant choisi
var ets;	// coor de l'éts pour centrer la carte
var startName;	// coor de départ
var endName;	// coor d'arrivée
var markerResto;
var stepDisplay;	// array contenant les infos a afficher pour un marqueur 'step'
var infowindow;		// fenetres contenantles infos des restaurants
var directionsDisplay;	// display pour google
var directionsService;	// service pour google
var request;	// la requete lancée pour calculer le trajet
var mapOptions;	// les options liés a la carte
var imageMarkerResto;	// image pour personnaliser les marqueurs
var map; // la map utilisée 


$(function() {
	$(document).on("click", ".choixCommande", function() {
		var commandeId = event.target.getAttribute('data-commandeId');
		
		var viewUrl = '/commandes/choisir_commande/' + commandeId;
		
		$.get(viewUrl, function(data) {
			if (data == 'success') {
				window.location.href = "/livreurs/mes_commandes/";
			}
			else {
				alert(data);
			}
		});
	});
});

function initialize() {

	var ets = new google.maps.LatLng(45.4953573,-73.5630168);

	imageMarkerResto = "/static/images/restaurant.png";
	mapOptions = { zoom:12, center:ets};
	map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);
	directionsService = new google.maps.DirectionsService();
	directionsDisplay = new google.maps.DirectionsRenderer();
	directionsDisplay.setMap(map);
	directionsDisplay.setPanel(document.getElementById('directions-panel'));
	// Instantiate an info window to hold step text.
	stepDisplay = new google.maps.InfoWindow();
	getArrayPlacesSmall();
	
}

function getArrayPlacesSmall(){
	// ici on recevra les infos necessaires depuis le serveur

	console.log("DANS PLACES");
	//{"result": "success", "restos": [{"nom": "Restaurant1", "adresse": "station angrignon", "telephone": "555-555-5555"}]}
	
	$(function(){
		$.getJSON("http://127.0.0.1:8080/restaurants/getjson", function(result){			
			console.log(result);
			setRestoMarker(result.restos);
		});
	})
	
	//var places = [// [nom. adresseResto, telephoneResto, [tableau de tableau[ des commandes[id, adresseResto]]]]
	//              ['ets', 'ETS, Montreal, QC', '450-985-4871', [[1,'beauharnois'],[2,'15 St-Jean chateauguay']]],
	//              ['1000 Rue de la Gauchetière', '1000 Rue de la Gauchetière, Montreal, QC, ', '584-965-8745', [[1,'beauharnois'],[2,'chateauguay'],[3,'1111 Lapierre']]],
	//              ['Station Angrignon', 'Station Angrignon Montreal, QC', '541-985-3214', [[1,'beauharnois'],[2,'chateauguay'],[3,'1111 Lapierre']]],
	//              ['Station Bonaventure', 'Station Bonaventure Montreal, QC', '450-934-4961', [[1,'beauharnois'],[2,'chateauguay'],[3,'1111 Lapierre'],[4,'1024 Boul Laval']]]
	//             ];
	//return places;
}

function setRestoMarker(places){

	var nbPlaces = places.length;
	var geoCodedMarker;
	var geocoder = new google.maps.Geocoder();
	var markerResto;

	for (i = 0; i < nbPlaces; i++){

		var nomResto = places[i].nom;
		var adresseResto = places[i].adresse;
		var telephoneResto = places[i].telephone;
		//var nbCommandesPretes = places[i][3].length;


		var contentString = '<div id="content">'+
		'</div>'+
		'<h1 id="firstHeading" class="firstHeading">'+nomResto+'</h1>'+
		'<div id="bodyContent">'+
		'<p><b>adresseResto: </b>'+ adresseResto +
		'<br/><b>Téléphone: </b>'+ telephoneResto + '</p>';
//		'<br/><b>Nombre de commandes prêtes: </b><a href="www.google.com">'+nbCommandesPretes+'</a></p>'+'';

		for (var j = 0; j < places[i].commandes.length; j++){
			// besoin des infos de la commande
			var idCommande = places[i].commandes[j].id;
			var nomDestination = places[i].commandes[j].adresse;

			contentString = contentString.concat("<br/>"+idCommande+": "+nomDestination+"  " +"<button type='submit' data-commandeId='" + idCommande + "' class='choixCommande' name='choixCommande' onClick='showTrajectory(\""+adresseResto+"\",\""+nomDestination+"\")' value="+idCommande+"> Voir </button> <button type='submit' data-commandeId='" + idCommande + "' class='choixCommande' name='choixCommande' onClick='choisirCommande(\""+nomResto+"\",\""+adresseResto+"\",\""+nomDestination+"\",\""+idCommande+"\")' value="+idCommande+"> Choisir </button>");
		}

		geocoder.geocode({'address': adresseResto}, function(nomResto, contentString) {
			return (function(results, status) {
				if (status == google.maps.GeocoderStatus.OK) {
					markerResto = new google.maps.Marker({
						position: results[0].geometry.location,
						map:map,
						title: nomResto,
						icon: imageMarkerResto
					});
					addMarkerListener(markerResto, contentString);
				}
			});
		}(nomResto, contentString));
	}
}

function addMarkerListener(marker, contentString){
	google.maps.event.addListener(marker, 'click', function() {
		
		closeInfoWindow();
		
		infowindow = new google.maps.InfoWindow({ content: contentString });
		addInfoWindowListener(infowindow);
		infowindow.open(map,marker);
		hideRestoMarkers(marker);
	});
	restoMarkerArray.push(marker);
}



function addInfoWindowListener(infowindow){
	google.maps.event.addListener(infowindow, 'closeclick', function() {
		showAllRestoMarkers();
	});
}



function showAllRestoMarkers(){
	for (var mu = 0; mu < restoMarkerArray.length; mu++) {
		restoMarkerArray[mu].setVisible(true);
	}
}



function hideRestoMarkers(marker){
	restoMarkerArray[0].setVisible(false);
	for (var mu = 0; mu < restoMarkerArray.length; mu++) {
		restoMarkerArray[mu].setVisible(false);
	}
	marker.setVisible(true);
}



function toggleAllMarkers(etat){
	
	if(etat){
		document.getElementById('toggleMarqueurs').innerHTML = '<input type="button" value="Cacher Marqueurs" onclick="toggleAllMarkers(false);" />';
	}
	else{
		document.getElementById('toggleMarqueurs').innerHTML = '<input type="button" value="Voir Marqueurs" onclick="toggleAllMarkers(true);" />';
	}
	
	for (var mu = 0; mu < restoMarkerArray.length; mu++) {
		restoMarkerArray[mu].setVisible(etat);
	}
	
	for (var mu = 0; mu < markerArray.length; mu++) {
		markerArray[mu].setVisible(etat);
	}
}

function closeInfoWindow(){
	if (infowindow) {
		infowindow.close();
	}
}


function choisirCommande(nomResto, adresseResto, nomDestination, idCommande){

	// retrouver le restaurant selon l'adresse ou le nom
	// dire au systeme que la commande a été prise et quelle est partie.
	console.log("LA COMMANDE A ETE CHOISIE ET N'EST PLUS DISPONIBLE")
	// appeller showTrajectory pour afficher le chemin
}

function showTrajectory(adresseResto, nomDestination){
	document.getElementById("directions-panel").innerHTML = '<div class="positionDepart"> <h1> Choisir origine</h1>'+
	'<b>Origine:</b> <input type="text" id="positionDepartLivraison" /> <br/>'+
	'<input type="button" value="Trouve Moi!" onclick="findMe(\''+adresseResto+'\',\''+nomDestination+'\');" /> </div>';
}

function findMe(adresseResto, nomDestination){
	closeInfoWindow();

	var positionDepartLivraison;
	 positionDepartLivraison = document.getElementById('positionDepartLivraison').value;
	
	 console.log("position:" + positionDepartLivraison);
	 
	if(positionDepartLivraison){
		 console.log("2222222");

		buildRequest(positionDepartLivraison, nomDestination, adresseResto);
	}
	else{
		 console.log("else");

		// Try HTML5 geolocation
		if(navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(function(position) {
				var pos = new google.maps.LatLng(position.coords.latitude,
						position.coords.longitude);
				buildRequest(pos, nomDestination, adresseResto);
		
			}, function() {
				handleNoGeolocation(true);
				buildRequest(new google.maps.LatLng(60, 105), nomDestination, adresseResto);
			});
		} else {
			// Browser doesn't support Geolocation
			handleNoGeolocation(false);
			buildRequest(new google.maps.LatLng(60, 105), nomDestination, adresseResto);
		}
	}
}


function handleNoGeolocation(errorFlag) {
	if (errorFlag) {
		var content = 'Error: The Geolocation service failed.';
	} else {
		var content = 'Error: Your browser doesn\'t support geolocation.';
	}
	console.log(content);
}


function buildRequest(startName, endName, waypointNameParam){

	// si des parametres sont passés on les prend, sinon on prend les textbox
	if(startName == null){
		startName = document.getElementById('start').value;
	}
	if(endName == null){
		endName = document.getElementById('end').value;
	}
	
	if(waypointNameParam){ // si passe en param
		console.log("waypoint dans param");
		request = createRequestWithWaypoint(startName, endName, waypointNameParam);
		console.log(startName);
		console.log(endName);
		console.log(request);
		
	}else if(document.getElementById('waypoint').value){ // si par id
		var waypointParId = document.getElementById('waypoint').value;
		console.log("waypoint dans id:"); 
		request = createRequestWithWaypoint(startName, endName, waypointParId);
	}
	else{ // si pas de waypoint
		console.log("pas waypoint");
		request = {
				origin : startName,
				destination : endName,
				travelMode : google.maps.TravelMode.DRIVING
		};
	}
	calcRoute(request);
	waypoint.length = 0;
	closeInfoWindow();
}


function createRequestWithWaypoint(startName, endName, waypointName){
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
	return request;
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
		stepDisplay.setContent(text);
		stepDisplay.open(map, marker);
	});
}


google.maps.event.addDomListener(window, 'load', initialize);
