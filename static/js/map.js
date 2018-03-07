



window.addEventListener( 'load', getZipCode )


function getZipCode( ) {
	// Omit irrelevent console log error harassment
	if ( document.getElementById( 'map' ) ) {
		var http = new XMLHttpRequest( )
		http.onreadystatechange = function( ) {
			if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
				// Search geocode data that matches zip code
				viewGeocode( new google.maps.Geocoder( ), http.responseText )
			}
		}
		http.open( 'GET', '/data' )
		http.send( )
	}
}

function drawMap( coords, zipcode ) {
	// Avoid annoying, meaningless console errors
	if ( coords ) {
		// View location details used for api mapping
		console.log( 'ZipCode: ' + zipcode )
		console.log( 'Location:', coords )
		// Example coordinates for the Seattle area
		var seattle = new google.maps.LatLng( 47.6029432, -122.332146 )
		// Instantiate new interactive map from api
		var map = new google.maps.Map(
			document.getElementById( 'map' ),
			{ center: coords, zoom: 11 }
		)
		// Look up farmers' markets in the vicinity
		browseMarkets( map, coords )
	}
}

function browseMarkets( map, coords ) {
	// Map out markets in the area via a search object
	var seeker = new google.maps.places.PlacesService( map )
	// Parameters for searches within the zip code's region
	/* var area = { location: coords, radius: '250', keyword: 'market' } */
	var zone = { location: coords, radius: '250', query: 'farmers market' }
	// Hold generated market tooltips in array for future viewing
	var views = [ ]
	// Broken search meant to be based on proximity
	/* seeker.nearbySearch( area, function( markets, status ) {
		if ( status == google.maps.places.PlacesServiceStatus.OK ) {
			// Nearby farmers markets, but not working yet
			console.log( 'NEAR Markets:', markets )
			// Distribute upon the map market location tooltips
			for ( var idx = 0; idx < markets.length; idx++ ) {
				var view = createLocation( markets[ idx ], map )
				views.push( view )
				// Sort through the list of generated tooltips
				if ( idx + 1 === markets.length ) {
					console.log( views )
				}
			}
		}
	} ) */
	// Find markets in the region through text searching
	seeker.textSearch( zone, function( markets, status ) {
		if ( status == google.maps.places.PlacesServiceStatus.OK ) {
			// Query api for markets and show resulting array
			console.log( 'TEXT Markets:', markets )
			// Read through markets and place them on the map
			for ( var idx = 0; idx < markets.length; idx++ ) {
				var view = createLocation( markets[ idx ], map )
				views.push( view )
				// Use previous array to view all created tooltips
				if ( idx + 1 === markets.length ) {
					console.log( views )
				}
			}
		}
	} )
}

function createLocation( market, map ) {
	// Make custom marker tooltips class accessible
	ViewClass( )
	// Create a new market location identifier on the map
	/* var location = new google.maps.Marker( {
		map: map,
		position: market.geometry.location.toJSON( ),
		title: market.name
	} ) */
	// Insert new custom market tooltips onto the map
	farmerMarket = new View( market.geometry.location, market )
	farmerMarket.setMap( map )
	// Give tooltip back to previous function to log result
	return farmerMarket
}


