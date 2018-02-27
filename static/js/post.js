



var http = new XMLHttpRequest( )


window.addEventListener( 'load', grabData )


function grabData( ) {
	if ( document.getElementById( 'assign' ) ) {
		// Generate click event on identified button
		document.getElementById( 'assign' ).onclick = function( ) {
			// Value from input field used for post method
			var zipcode = document.getElementById( 'zipcode' ).value
			hostData( zipcode )
		}
	}
}

function hostData( zipcode ) {
	http.onreadystatechange = returnData
	// See if script is ran on click by logging the below
	console.log( 'Ajax JavaScript POST' )
	http.open( 'POST', '/post' )
	// Declare request header's MIME type before sending
	http.setRequestHeader( 'Content-Type', 'text/plain' )
	// Format/encode data to ensure server can parse it
	http.send( encodeURIComponent( zipcode ) )
}

function returnData( ) {
	if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
		console.log( 'POST Response: ' + http.response )
	}
}


