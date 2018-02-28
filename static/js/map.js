



// Prototyping Google Maps api interaction



var map


window.addEventListener( 'load', drawMap )


function drawMap( ) {
	// Set example coordinates to Seattle
	var seattle = new google.maps.LatLng( 47.5429432, -122.382146 )
	// Generate interactive map from api
	map = new google.maps.Map(
		document.getElementById( 'map' ),
		{ center: seattle, zoom: 11 }
	)
}


