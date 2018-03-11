



import json
from marketmeals import db
from marketmeals.location.utils import html, urlify, catalog
from marketmeals.location.models import Market
from flask import Blueprint, request, render_template, redirect, url_for, session



location = Blueprint( 'location', __name__, template_folder = html )



@location.route( '/url', methods = [ 'POST' ] )
def url( ):
	session[ 'market' ] = json.loads( request.data.decode( 'utf-8' ) )
	print( 'MARKET ' + session[ 'market' ][ 'name' ] )
	session[ 'url' ] = urlify( session[ 'market' ][ 'name' ] )
	print( 'NEWURL ' + session[ 'url' ] )
	url = Market.query.filter_by( url = session[ 'url' ] ).first( )
	if url is None:
		market = catalog( session[ 'market' ][ 'name' ], session[ 'url' ], session[ 'market' ][ 'address_components' ] )
		db.session.add( market )
		db.session.commit( )
	return session[ 'url' ]


@location.route( '/market/<market>', methods = [ 'GET', 'POST' ] )
def market( market ):
	print( 'Arrived at Market!' )
	market = market
	return render_template( 'location/market.html', market = session[ 'market' ] )


