



var http = new XMLHttpRequest( )


window.addEventListener( 'load', loadData )


function loadData( ) {
	if ( document.getElementById( 'query' ) ) {
		// Allow button element to initialize query
		document.getElementById( 'query' ).onclick = function( ) {
			insertData( )
		}
	}
}

function insertData( ) {
	http.onreadystatechange = queryData
	// Go insert data into database from backend
	http.open( 'POST', '/query' )
	http.send( )
}

function queryData( ) {
	if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
		// View database insertion if successful
		console.log( 'SQL Query: ' + http.response )
	}
}



