



// Prototyping Google Maps api interaction



window.addEventListener( 'load', getZipCode )


function getZipCode( ) {
	var http = new XMLHttpRequest( )
	http.onreadystatechange = function( ) {
		if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
			console.log( 'ZipCode HTTP: ' + http.responseText )
			// Load map before passing the zipcode
			document.getElementById( 'map' ).onload = drawMap( http.responseText )
		}
	}
	http.open( 'GET', '/data' )
	http.send( )
}

function drawMap( zipcode ) {
	// Avoid annoying, meaningless console errors
	if ( zipcode ) {
		console.log( 'ZipCode API: ' + zipcode )
		// Example coordinates for the Seattle area
		var seattle = new google.maps.LatLng( 47.6029432, -122.332146 )
		// Generate new interactive map from the api
		var map = new google.maps.Map(
			document.getElementById( 'map' ),
			{ center: seattle, zoom: 11 }
		)
	}
}


