



// Preview customized market popup previews using a View class



function ViewClass( ) {
	
	// View class constructor for new custom views
	View = function( coords, element ) {
		// Designate coordinates for positioning the view
		this.coords = coords
		// Verify that the view can attach to an element
		if ( !element ) {
			element = document.createElement( 'div' )
			element.classList.add( 'content' )
			element.innerText = 'FARMERS MARKET'
		}
		// Name the view's class to should be applied to it
		element.classList.add( 'popup-bubble-content' )
		// Positions the view just above its location pointer
		var offset = document.createElement( 'div' )
		offset.classList.add( 'popup-bubble-anchor' )
		offset.appendChild( element )
		// Generate anchor element to contain view objects
		this.anchor = document.createElement( 'div' )
		this.anchor.classList.add( 'popup-tip-anchor' )
		this.anchor.appendChild( offset )
		// Optionally stop events from affecting the map
		this.stopEventPropagation( )
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
			'wheel',
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
	
}



