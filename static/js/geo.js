



// Modularizing geocode behavior by splitting into a separate file



function viewGeocode( geocode, zipcode ) {
	// Stifle meaningless unfound reference console error
	if ( window.location.pathname === '/' + zipcode ) {
		geocode.geocode( {
				address: zipcode,
				componentRestrictions: { postalCode: zipcode },
				region: '021'
			},
			function( geodata, feedback ) {
				if ( feedback === 'OK' ) {
					var coords = geodata[ 0 ].geometry.location.toJSON( )
					console.log( 'Geocode:', geodata[ 0 ] )
					drawMap( coords, zipcode )
				}
				else {
					console.error( 'There was a problem trying to geocode!  ' + feedback )
					window.location.pathname = ''
				}
			}
		)
	}
}

function reverseGeocode( geocode, market ) {
	// Inspect the received market data that will be used
	console.log( market )
	// Find the location details based on the market's id
	geocode.geocode( {
			placeId: market.place_id
		},
		function( geodata, feedback ) {
			if ( feedback === 'OK' ) {
				console.log( geodata )
			}
			else {
				console.error( 'An error occurred while reverse geocoding!  ' + feedback )
			}
		}
	)
}



