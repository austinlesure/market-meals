



// Exploring data retrieval from the Flask backend to the frontend



var http = new XMLHttpRequest( )

// Initiate http request once page is loaded
window.onload = fetchData
// Verify successful script call
console.log( 'At the script!' )


// Send request to server and react to feedback
function fetchData( ) {
	http.onreadystatechange = viewData
	http.open( 'GET', '/core' )
	http.send( )
}

// Prepare and output response if successful
function viewData( ) {
	if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
		console.log( http.response )
	}
}


