



// Exploring http get request data retrieval from the Flask backend to the frontend



var http = new XMLHttpRequest( )


// Initiate get method once page is loaded
window.addEventListener( 'load', fetchData )


// Send request to server and react to feedback
function fetchData( ) {
	http.onreadystatechange = viewData
	// Verify successful script call
	console.log( 'Ajax JavaScript GET' )
	http.open( 'GET', '/get' )
	http.send( )
}

// Prepare and output response if successful
function viewData( ) {
	if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
		console.log( 'GET Response: ' + http.response )
	}
}



