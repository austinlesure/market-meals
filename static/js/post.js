



// Making http post request to the Flask backend and returning response to frontend



var http = new XMLHttpRequest( )


// Initiate post method once page is loaded
window.addEventListener( 'load', grabData )


// Generate click event on identified button
function grabData( ) {
	document.getElementById( 'assign' ).onclick = function( ) {
		// Value from input field used for post method
		var zipcode = document.getElementById( 'zipcode' ).value
		// Execute the post http request and send data
		hostData( zipcode )
	}
}

// Post request for passing data to server
function hostData( zipcode ) {
	http.onreadystatechange = returnData
	// See if script is ran on click by logging the below
	console.log( 'From another script!' )
	http.open( 'POST', '/post' )
	// Declare request header's MIME type before sending
	http.setRequestHeader( 'Content-Type', 'text/plain' )
	// Format/encode data to ensure server can parse it
	http.send( encodeURIComponent( zipcode ) )
}

// Output server's response to post method
function returnData( ) {
	if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
		console.log( 'It liked the ' + http.response + '!' )
	}
}


