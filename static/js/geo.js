



// Modularizing geocode behavior by splitting into a separate file



function viewGeocode( zipcode ) {
	// Stifle meaningless unfound reference console error
	if ( window.location.pathname === '/' + zipcode ) {
		// Geocode location data based upon zip code input
		var geo = new google.maps.Geocoder( )
		geo.geocode( {
				address: zipcode,
				componentRestrictions: { postalCode: zipcode },
				region: '021'
			},
			function( geodata, feedback ) {
				if ( feedback === 'OK' ) {
					// Transform location into json for portability
					var coords = geodata[ 0 ].geometry.location.toJSON( )
					// Output geocode objects found via zip code
					console.log( 'Geocode:', geodata[ 0 ] )
					// Utilize geocode results to render map contents
					drawMap( coords, zipcode )
				}
				else {
					// Watch for and redirect on geocoding errors
					console.error( 'There was a problem!  ' + feedback )
					window.location.pathname = ''
				}
			}
		)
	}
}

function reverseGeocode( market ) {
	// Inspect the received market data that will be used
	console.log( market )
}


