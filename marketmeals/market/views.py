



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
	print( market )
	print( session[ 'url' ] )
	print( Market.query.filter_by( url = market ).first( ) )
	if market == session[ 'url' ] or Market.query.filter_by( url = market ).first( ):
		print( 'Market!' )
		return render_template( 'market/market.html', market = session[ 'market' ] )
	else:
		print( 'Bad!' )
		return redirect( '/' )


## View method commented out originally from templates branch
""" @market.route( '/join', methods = [ 'GET' ] )
def join( ):
	farmers = [ ]
	recipes = [ ]
	identifiers = {  } """
	## Grabbing market via get request from the url most likely
	""" market = request.args.get( 'market' )
	if market:
		market = Market.query.filter_by( name = market ).first( ) """
		## Linking farmers with markets, so use farmer_days table
		""" days = FarmerMarketLink.query.filter_by( market_id = market.market_id ).all( )
		for day in days:
			farmer = Farmer.query.filter_by( farmer_id = day.farmer_id ).first( )
			pid = farmer.farmer_id
			farmers.append( farmer ) """
			## Obtain the farmer's goods to be for sale at the market
			## Replace by querying the farmer_products table instead
			""" merch = FarmerProductLink.query.filter_by( farmer_id = farmer.farmer_id ).all( )
			for good in merch:
				product = Product.query.filter_by( product_id = good.product_id ).first( ) """
				## Query the more semantic ingredients table for querying
				""" for ingredient in get_recipe_products( ):
					if ingredient.product_id == product.product_id:
						if ingredient not in recipes:
							recipes.append( Recipe.query.filter_by( recipe_id = ingredient.recipe_id ).first( ) ) """
				## Seems to be collecting farmer ids for a certain purpose
				""" if pid in identifiers:
					identifiers[ pid ].append( product )
				else: """
					## Pretty sure this creates a 2D list for no good reason
					""" identifiers[ pid ] = [ product ] """
		## Badly needs trimming down via a context dictionary variable
		""" return render_template(
			'market/join.html',
			market = market,
			farmers = farmers,
			categories = get_prodcats( ),
			dic = dic,
			recipes = recipes
		)
	else:
		return redirect( '/' ) """



