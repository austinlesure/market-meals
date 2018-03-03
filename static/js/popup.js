



// View customized market tooltips using a Market class



function defineMarketClass( ) {
	
	// Market class constructor for new custom tooltips
	Market = function ( position, content ) {
		// Designate coordinates for positioning the tooltip
		this.position = position
		// Verify that the tooltip can attach to an element
		if ( !content ) {
			content = document.createElement( 'div' )
			content.classList.add( 'content' )
			content.innerText = 'FARMERS MARKET'
		}
		// Name the tooltip's class to should be applied to it
		content.classList.add( 'popup-bubble-content' )
		// Positions the tooltip just above its location pointer
		var pixelOffset = document.createElement( 'div' )
		pixelOffset.classList.add( 'popup-bubble-anchor' )
		pixelOffset.appendChild( content )
		// Generate anchor element to contain tooltip objects
		this.anchor = document.createElement( 'div' )
		this.anchor.classList.add( 'popup-tip-anchor' )
		this.anchor.appendChild( pixelOffset )
		// Optionally stop events from affecting the map
		this.stopEventPropagation( )
	}
	
	
	// Use api's OverlayView for using custom markers
	Market.prototype = Object.create( google.maps.OverlayView.prototype )
	
	// Add the tooltip on the map to display markets
	Market.prototype.onAdd = function ( ) {
		this.getPanes( ).floatPane.appendChild( this.anchor )
	}
	
	// Remove tooltip from the map when finished
	Market.prototype.onRemove = function ( ) {
		if ( this.anchor.parentElement ) {
			this.anchor.parentElement.removeChild( this.anchor )
		}
	}
	
	// Calculate necessary tooltip positional specifications
	Market.prototype.draw = function ( ) {
		// Translate market coordinates into pixel positions
		var divPosition = this.getProjection( ).fromLatLngToDivPixel( this.position )
		// Hides tooltip when far from view, but it's broken
		var display = Math.abs( divPosition.x ) < 4000 && Math.abs( divPosition.y ) < 4000 ? 'block' : 'none'
		// Likely affects the positioning of market tooltips
		if ( display === 'block' ) {
			this.anchor.style.left = divPosition.x + 'px'
			this.anchor.style.top = divPosition.y + 'px'
		}
		if ( this.anchor.style.display !== display ) {
			this.anchor.style.display = display
		}
	}
	
	// Stops user behavior from interfering with the map
	Market.prototype.stopEventPropagation = function ( ) {
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
		events.forEach( function ( event ) {
			anchor.addEventListener( event, function ( e ) {
				e.stopPropagation( )
			} )
		} )
	}
	
}



