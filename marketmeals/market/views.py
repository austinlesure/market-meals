



import re
import json
from marketmeals import db
from marketmeals.market.utils import html, urlify, catalog
from marketmeals.market.models import Market
from flask import Blueprint, request, render_template, redirect, url_for, session



market = Blueprint( 'market', __name__, template_folder = html )



@market.route( '/url', methods = [ 'POST' ] )
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


@market.route( '/market/<market>', methods = [ 'GET', 'POST' ] )
def view( market ):
	print( 'Arrived at Market!' )
	if re.match( r'^([a-z]+-)*(market){1}(-[a-z]+)*$', market ):
		print( 'Market!' )
		market = market
		return render_template( 'market/market.html', market = session[ 'market' ] )
	else:
		return redirect( '/' )



