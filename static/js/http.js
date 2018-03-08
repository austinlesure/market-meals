



var http = new XMLHttpRequest( )


window.addEventListener( 'load', getZipCode )


function getZipCode( ) {
	if ( document.getElementById( 'map' ) ) {
		http.onreadystatechange = function( ) {
			if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
				viewGeocode( new google.maps.Geocoder( ), http.responseText )
			}
		}
		http.open( 'GET', '/zone' )
		http.send( )
	}
}

function exportJson( amalgam ) {
	http.onreadystatechange = function( ) {
		if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
			console.log( 'Response: ', http.responseText )
			var extra = document.getElementsByClassName( 'extra' )[ 0 ]
			extra.setAttribute( 'action', '/' + http.responseText )
			var visit = document.getElementsByClassName( 'visit' )[ 0 ]
			console.log( extra )
			console.log( visit )
			var url = document.createElement( 'input' )
			url.setAttribute( 'type', 'hidden' )
			url.setAttribute( 'name', 'url' )
			url.setAttribute( 'value', http.responseText )
			extra.insertBefore( url, visit )
		}
	}
	http.open( 'POST', '/url' )
	http.setRequestHeader( 'Content-Type', 'application/json' )
	http.send( JSON.stringify( amalgam ) )
}



