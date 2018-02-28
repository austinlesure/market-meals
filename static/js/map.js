



// Prototyping Google Maps api interaction



window.addEventListener( 'load', getZipCode )


function getZipCode( ) {
	var http = new XMLHttpRequest( )
	http.onreadystatechange = function( ) {
		if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
			// Load map before passing the zipcode
			console.log( 'ZipCode1: ' + http.response )
			document.getElementById( 'map' ).onload = drawMap( http.response )
		}
	}
	http.open( 'GET', '/data' )
	http.send( )
}

function drawMap( zipcode ) {
	if ( zipcode ) {
		console.log( 'ZipCode2: ' + zipcode )
		// Set example coordinates to Seattle
		var seattle = new google.maps.LatLng( 47.6029432, -122.332146 )
		// Generate interactive map from api
		var map = new google.maps.Map(
			document.getElementById( 'map' ),
			{ center: seattle, zoom: 11 }
		)
	}
}



