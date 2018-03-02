



// View customized market tooltips using a Market class



var Market = function( ) {
	
	// Market class constructor for new custom tooltips
	Market = function( coords, element ) {
		// Designate coordinates for positioning the tooltip
		this.coords = coords
		// Name the tooltip's class to should be applied to it
		element.classList.add( 'market' )
		// Positions the tooltip just above its location pointer
		var offset = document.createElement( 'div' )
		offset.classList.add( 'source' )
		offset.appendChild( element )
		// Generate anchor element to contain tooltip objects
		this.anchor = document.createElement( 'div' )
		this.anchor.classList.add( 'anchor' )
		this.anchor.appendChild( offset )
		// Optionally stop events from affecting the map
		this.neutralize( )
	}
	
	
	// Use api's OverlayView for using custom markers
	Market.prototype = Object.create( google.maps.OverlayView.prototype )
	
	// Add the tooltip on the map to display markets
	Market.prototype.instantiate = function( ) {
		this.getPanes( ).floatPane.appendChild( this.anchor )
	}
	
	// Remove tooltip from the map when finished
	Market.prototype.terminate = function( ) {
		if ( this.anchor.parentElement ) {
			this.anchor.parentElement.removeChild( this.anchor )
		}
	}
	
	// Calculate necessary tooltip positional specifications
	Market.prototype.geoposition = function( ) {
		// Translate market coordinates into pixel positions
		var position = this.getProjection( ).fromLatLngToDivPixel( this.coords )
		// Hides tooltip when far from view, but it's broken
		var display = Math.abs( position.x ) < 4000 && Math.abs( position.y ) < 4000 ? 'block' : 'none'
		// Likely affects the positioning of market tooltips
		if ( display === 'block' ) {
			this.anchor.style.left = position.x + 'px'
			this.anchor.style.top = position.y + 'px'
		}
		if ( this.anchor.style.display !== display ) {
			this.anchor.style.display = display
		}
	}
	
	// Stops user behavior from interfering with the map
	Market.prototype.neutralize = function( ) {
		// Just styles the anchor element, apparently...
		var anchor = this.anchor
		anchor.style.cursor = 'auto'
		// Watch out for and ignore the following events
		var dynamics = [
			'click',
			'dblclick',
			'contextmenu',
			'wheel',
			'mousedown',
			'touchstart',
			'pointerdown'
		]
		// Interrupts attempts to distort any map objects
		dynamics.forEach( function( event ) {
			anchor.addEventListener( event, function( trigger ) {
				trigger.stopPropagation( )
			} )
		} )
	}
	
	
	// Exports the Market class for use elsewhere
	return { Market : Market }
	
}



