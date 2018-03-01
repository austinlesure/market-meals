



// Prototyping Google Maps api use - needs behavior to handle no geocode results



window.addEventListener( 'load', getZipCode )


function getZipCode( ) {
	var http = new XMLHttpRequest( )
	http.onreadystatechange = function( ) {
		if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
			console.log( 'ZipCode HTTP: ' + http.responseText )
			// Load map before passing the zipcode
			document.getElementById( 'map' ).onload = drawMap( http.responseText )
		}
	}
	http.open( 'GET', '/data' )
	http.send( )
}

function drawMap( zipcode ) {
	// Avoid annoying, meaningless console errors
	if ( zipcode ) {
		console.log( 'ZipCode API: ' + zipcode )
		// Non-functional fetching of geocode objects
		var zone = viewGeocode( zipcode )
		console.log( 'Geocode is... ' + zone )
		// Example coordinates for the Seattle area
		var seattle = new google.maps.LatLng( 47.6029432, -122.332146 )
		// Generate new interactive map from the api
		var map = new google.maps.Map(
			document.getElementById( 'map' ),
			{ center: seattle, zoom: 11 }
		)
	}
}

function viewGeocode( zipcode ) {
	console.log( 'ZipCode GEO: ' + zipcode )
	// Build the geocoder object for geocode lookups
	var geo = new google.maps.Geocoder( )
	// Record geolocation data using the given zip code
	var code = geo.geocode( {
			address: zipcode,
			componentRestrictions: { postalCode: zipcode },
			region: '021'
		},
		function( data, fate ) {
			if ( fate == 'OK' ) {
				data.forEach( element => {
					// Inspect the single geocode element in full
					console.log( element )
					// Transform location into json for portability
					var coord = element.geometry.location.toJSON( )
					console.log( 'JSON Location:', coord )
					// View location coordinates in greater detail
					console.log( 'LatLng Location: ' + element.geometry.location )
					console.log( '    Latitude: ' + element.geometry.location.lat( ) )
					console.log( '    Longitude: ' + element.geometry.location.lng( ) )
				} )
			}
			// Watch and report on any errors from geocoding
			else {
				console.log( 'There was a problem!  ' + fate )
			}
		}
	)
}



