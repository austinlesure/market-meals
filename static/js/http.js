



var http = new XMLHttpRequest( )


window.addEventListener( 'load', getZipCode )


function getZipCode( ) {
	if ( document.getElementById( 'map' ) ) {
		http.onreadystatechange = function( ) {
			if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
				viewGeocode( new google.maps.Geocoder( ), http.responseText )
			}
		}
		http.open( 'GET', '/data' )
		http.send( )
	}
}

function exportJson( amalgam ) {
	http.onreadystatechange = function( ) {
		if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
			console.log( 'Response: ', http.response )
		}
	}
	http.open( 'POST', '/json' )
	http.setRequestHeader( 'Content-Type', 'application/json' )
	http.responseType = 'json'
	http.send( JSON.stringify( amalgam ) )
}


