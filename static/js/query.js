



// Use an event listener on an html element to stop script overrides



var http = new XMLHttpRequest( )


window.addEventListener( 'load', insertData )


function insertData( ) {
	http.onreadystatechange = queryData
	// Go insert data into database
	http.open( 'POST', '/query' )
	http.send( )
}

function queryData( ) {
	if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
		// View database insertion
		console.log( 'SQL Query: ' + http.response )
	}
}


