



function viewGeocode( geocode, zipcode ) {
	var scope = { address: zipcode, componentRestrictions: { postalCode: zipcode }, region: '021' }
	geocode.geocode( scope, function( geodata, feedback ) {
		if ( feedback === 'OK' ) {
			var coords = geodata[ 0 ].geometry.location.toJSON( )
			console.log( 'Geocode:', geodata[ 0 ] )
			drawMap( coords, zipcode )
		}
		else {
			console.error( 'There was a problem trying to geocode!  ' + feedback )
			window.location.pathname = ''
		}
	} )
}

function reverseGeocode( geocode, market ) {
	console.log( market )
	var id = { placeId: market.place_id }
	geocode.geocode( id, function( geodata, feedback ) {
		if ( feedback === 'OK' ) {
			console.log( geodata )
		}
		else {
			console.error( 'An error occurred while reverse geocoding!  ' + feedback )
		}
	} )
}


