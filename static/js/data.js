



// Exploring data retrieval from the Flask backend to the frontend



// Immediately execute's the api request once page is loaded
window.onload = fetchData


// Making the request for requesting backend data
function fetchData( ) {
	// Http object which will handle api calls to the server via ajax 
	var http = new XMLHttpRequest( )
	// Request access to the server
	http.getData = function( ) {
		// Log the server response if successful
		if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
			console.log( http.response )
			// Not working yet
			console.log( 'SUCCESS!!!' )
		}
		else {
			// Also not working
			console.log( 'FAILURE!!!' )
		}
	}
	// Set http method, server url, and async status, then send request
	http.open( 'GET', '/core', true )
	http.send( )
	// Test successful script call
	console.log( 'From JavaScript' )
}


