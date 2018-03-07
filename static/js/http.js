



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

function grabData( ) {
	if ( window.location.pathname === '/' ) {
		document.getElementById( 'search' ).onclick = function( ) {
			var zipcode = document.getElementById( 'zipcode' ).value
			hostData( zipcode )
		}
	}
}

function hostData( zipcode ) {
	http.onreadystatechange = returnData
	console.log( 'Ajax JavaScript POST' )
	http.open( 'POST', '/post' )
	http.setRequestHeader( 'Content-Type', 'text/plain' )
	http.send( encodeURIComponent( zipcode ) )
}

function returnData( ) {
	if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
		console.log( 'POST Response: ' + http.response )
	}
}



