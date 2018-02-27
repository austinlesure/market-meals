



var http = new XMLHttpRequest( )


window.addEventListener( 'load', fetchData )


function fetchData( ) {
	http.onreadystatechange = viewData
	// Verify successful script call
	console.log( 'Ajax JavaScript GET' )
	http.open( 'GET', '/get' )
	http.send( )
}

function viewData( ) {
	if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
		console.log( 'GET Response: ' + http.response )
	}
}


