



import json
from marketmeals import db
from marketmeals.models import Market
from flask import Blueprint, request, render_template, redirect, url_for, session



farm = Blueprint( 'farm', __name__ )



@farm.route( '/url', methods = [ 'POST' ] )
def url( ):
	session[ 'market' ] = json.loads( request.data.decode( 'utf-8' ) )
	print( 'MARKET ' + session[ 'market' ][ 'name' ] )
	market = ''
	## Build url by lowercasing and hyphenating whitespace
	for char in session[ 'market' ][ 'name' ]:
		if char.isalnum( ):
			if char.isupper( ):
				market += char.lower( )
			else:
				market += char
		elif char.isspace( ):
			market += '-'
	print( 'NEWURL ' + market )
	session[ 'url' ] = market
	## Add new market to the database if not already recorded
	url = Market.query.filter_by( url = session[ 'url' ] ).first( )
	if url is None:
		street = ''
		city = ''
		state = ''
		zipcode = None
		for sub in session[ 'market' ][ 'address_components' ]:
			for area in sub[ 'types' ]:
				if area == 'street_number':
					street = sub[ 'short_name' ] + ' '
				## Some markets don't have route strings provided
				elif area == 'route':
					street += sub[ 'short_name' ]
				elif area == 'locality':
					city = sub[ 'short_name' ]
				## Incorrectly interpreting the shorter state value
				elif area == 'administrative_area_level_1':
					state = sub[ 'short_name' ]
				elif area == 'postal_code':
					zipcode = sub[ 'short_name' ]
		location = Market(
			name = session[ 'market' ][ 'name' ],
			url = session[ 'url' ],
			address_1 = street,
			city = city,
			state = state,
			zip_code = zipcode
		)
		db.session.add( location )
		db.session.commit( )
	return market


@farm.route( '/<market>', methods = [ 'GET', 'POST' ] )
def market( market ):
	print( 'Arrived at Market!' )
	market = market
	return render_template( 'market.html', market = session[ 'market' ] )



