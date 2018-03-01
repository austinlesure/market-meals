



window.addEventListener( 'load', getZipCode )


function getZipCode( ) {
	var http = new XMLHttpRequest( )
	http.onreadystatechange = function( ) {
		if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
			// Search for geocode data that matches zip code
			viewGeocode( http.responseText )
		}
	}
	http.open( 'GET', '/data' )
	http.send( )
}

function viewGeocode( zipcode ) {
	// Geocode location data based upon zip code input
	var geo = new google.maps.Geocoder( )
	geo.geocode( {
			address: zipcode,
			componentRestrictions: { postalCode: zipcode },
			region: '021'
		},
		function( geodata, fate ) {
			if ( fate == 'OK' ) {
				// Transform location into json for portability
				var coords = data[ 0 ].geometry.location.toJSON( )
				// Output geocode objects found via zip code
				console.log( 'Geocode:', geodata[ 0 ] )
				// Utilize geocode results to render map contents
				drawMap( coords, zipcode )
			}
			else {
				// Watch for and redirect on geocoding errors
				console.error( 'There was a problem!  ' + fate )
				window.location.pathname = ''
			}
		}
	)
}

function drawMap( geocode, zipcode ) {
	// Avoid annoying, meaningless console errors
	if ( geocode ) {
		// View location details used for api mapping
		console.log( 'ZipCode: ' + zipcode )
		console.log( 'Location:', geocode )
		// Example coordinates for the Seattle area
		var seattle = new google.maps.LatLng( 47.6029432, -122.332146 )
		// Instantiate new interactive map from api
		var map = new google.maps.Map(
			document.getElementById( 'map' ),
			{ center: geocode, zoom: 12 }
		)
	}
}



