



function ViewClass( ) {
	
	// View class constructor for new custom views
	View = function( coords, market ) {
		// Designate coordinates for positioning the view
		this.coords = coords
		// New html element for displaying view contents
		var element = document.createElement( 'div' )
		element.classList.add( 'view' )
		// Insert farmers market title into an h6 element
		var title = document.createElement( 'h6' )
		element.appendChild( title )
		title.innerText = market.name
		// Positions the view just above its location pointer
		var offset = document.createElement( 'div' )
		offset.classList.add( 'spike' )
		offset.appendChild( element )
		// Generate anchor element to contain view objects
		this.anchor = document.createElement( 'div' )
		this.anchor.classList.add( 'anchor' )
		this.anchor.appendChild( offset )
		// Optionally stop events from affecting the map
		this.stopEventPropagation( )
		// Make expandable panels for sharing extra info
		this.buildElements( market, element, offset )
	}
	
	
	// Use api's OverlayView for using custom markers
	View.prototype = Object.create( google.maps.OverlayView.prototype )
	
	
	// Add the view on the map to display markets
	View.prototype.onAdd = function( ) {
		this.getPanes( ).floatPane.appendChild( this.anchor )
	}
	
	// Remove view from the map when finished
	View.prototype.onRemove = function( ) {
		if ( this.anchor.parentElement ) {
			this.anchor.parentElement.removeChild( this.anchor )
		}
	}
	
	// Calculate necessary view positional specifications
	View.prototype.draw = function( ) {
		// Translate market coordinates into pixel positions
		var position = this.getProjection( ).fromLatLngToDivPixel( this.coords )
		// Hides view when zoomed far out, but it's broken
		var display = Math.abs( position.x ) < 4000 && Math.abs( position.y ) < 4000 ? 'block' : 'none'
		// Likely affects the positioning of market views
		if ( display === 'block' ) {
			this.anchor.style.left = position.x + 'px'
			this.anchor.style.top = position.y + 'px'
		}
		if ( this.anchor.style.display !== display ) {
			this.anchor.style.display = display
		}
	}
	
	// Stops user behavior from interfering with the map
	View.prototype.stopEventPropagation = function( ) {
		// Just styles the anchor element, apparently...
		var anchor = this.anchor
		anchor.style.cursor = 'auto'
		// Watch out for and ignore the following events
		var events = [
			'click',
			'dblclick',
			'contextmenu',
			'mousedown',
			'touchstart',
			'pointerdown'
		]
		// Interrupts attempts to distort any map objects
		events.forEach( function( event ) {
			anchor.addEventListener( event, function( reaction ) {
				reaction.stopPropagation( )
			} )
		} )
	}
	
	// Insert enlarged view frames into the html document
	View.prototype.buildElements = function( market, view, offset ) {
		// Create enlarged view to appear via activation
		var extra = document.createElement( 'div' )
		extra.classList.add( 'extra' )
		// Title header of farmers market inserted into frame
		var head = document.createElement( 'div' )
		extra.appendChild( head )
		var title = document.createElement( 'h3' )
		head.appendChild( title )
		title.innerText = market.name
		// Exits the expanded view and shrink it back down
		var retract = document.createElement( 'button' )
		head.appendChild( retract )
		retract.innerText = 'X'
		// Market address element added to larger view
		var address = document.createElement( 'p' )
		extra.appendChild( address )
		address.innerText = market.formatted_address
		// Go to the selected market's details page
		var visit = document.createElement( 'a' )
		extra.appendChild( visit )
		visit.innerText = 'View This Market'
		// Fetch reverse geocode market data before rerouting
		visit.addEventListener( 'click', function( ) {
			reverseGeocode( new google.maps.Geocoder( ), market )
		} )
		// Prepare event listeners onto larger view element
		this.expandView( extra, retract, view, offset )
	}
	
	// Open larger view frame to share additional info
	View.prototype.expandView = function( extra, retract, view, offset ) {
		// Locally saved preset variables of view object
		this.offset = offset
		this.view = view
		// Activation toggle to expose a larger frame
		view.addEventListener( 'click', function( ) {
			var open = document.getElementsByClassName( 'extra' )[ 0 ]
			if ( open ) {
				// Exit last opened window for a new one
				open.parentElement.firstChild.style.display = 'block'
				open.parentElement.removeChild( open )
			}
			// Won't restore if removed, so modify display
			view.style.display = 'none'
			offset.appendChild( extra )
		} )
		// Deactivation toggle for the larger info window
		retract.addEventListener( 'click', function( ) {
			view.style.display = 'block'
			offset.removeChild( extra )
			offset.appendChild( view )
		} )
	}
	
}


