



import json
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
	return market


@farm.route( '/<market>', methods = [ 'POST' ] )
def market( market ):
	market = market
	return render_template( 'market.html', market = session[ 'market' ] )



