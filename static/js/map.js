



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
	console.log( 'ZipCode: ' + zipcode )
	geo.geocode( {
			address: zipcode,
			componentRestrictions: { postalCode: zipcode },
			region: '021'
		},
		function( geodata, feedback ) {
			if ( feedback == 'OK' ) {
				// Transform location into json for portability
				var coords = geodata[ 0 ].geometry.location.toJSON( )
				// Output geocode objects found via zip code
				console.log( 'Geocode:', geodata[ 0 ] )
				// Utilize geocode results to render map contents
				browseMarkets( coords, zipcode )
			}
			else {
				// Watch for and redirect on geocoding errors
				console.error( 'There was a problem!  ' + feedback )
				window.location.pathname = ''
			}
		}
	)
}

function drawMap( coords, market ) {
	// Avoid annoying, meaningless console errors
	if ( coords && market ) {
		Market( )
		// View location details used for api mapping
		console.log( 'Location:', coords )
		// Example coordinates for the Seattle area
		var seattle = new google.maps.LatLng( 47.6029432, -122.332146 )
		// Instantiate new interactive map from api
		var map = new google.maps.Map(
			document.getElementById( 'map' ),
			{ center: coords, zoom: 10 }
		)
		// Design unique toolip marker for found markets
		market = new Market(
			market.geometry.location,
			document.getElementById( 'tooltip' )
		)
		console.log( market )
		market.setMap( map )
	}
}

function browseMarkets( coords, zipcode ) {
	var locale = new google.maps.Map(
		document.getElementById( 'map' ),
		{ center: coords, zoom: 10 }
	)
	// Map out markets in the area via a search object
	var seeker = new google.maps.places.PlacesService( locale )
	// Parameters for searches within he zip code's region
	var area = { location: coords, radius: '250', keyword: 'market' }
	var zone = { location: coords, radius: '250', query: 'farmers market' }
	// Broken search meant to be based on proximity
	seeker.nearbySearch( area, function( markets, status ) {
		if ( status == google.maps.places.PlacesServiceStatus.OK ) {
			// Nearby farmers markets, but not working yet
			console.log( 'NEAR Markets:', markets )
			console.log( markets[ 0 ] )
			createLocation( markets, locale, coords )
		}
	} )
	// Find markets in the region through text searching
	seeker.textSearch( zone, function( markets, status ) {
		if ( status == google.maps.places.PlacesServiceStatus.OK ) {
			// Query api for markets and show resulting array
			console.log( 'TEXT Markets:', markets )
			console.log( markets[ 0 ] )
			createLocation( markets, locale, coords )
		}
	} )
}

function createLocation( markets, locale, coords ) {
	if ( markets && locale ) {
		// Create a new market location identifier on the map
		/* var location = new google.maps.Marker( {
			map: map,
			position: market.geometry.location.toJSON( ),
			title: market.name
		} ) */
		drawMap( coords, markets[ 0 ] )
	}
}



