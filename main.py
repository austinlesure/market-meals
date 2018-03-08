



import re
import json as jsonx
from app import app, db
from flask import render_template, redirect, url_for, request, session
from models import Farmer, Market, Category, FarmerProduct
from hashutils import check_pw_hash



@app.route( '/', methods = [ 'GET', 'POST' ] )
def index( ):
	if request.method == 'GET':
		return render_template( 'index.html' )
	## Unused method, but temporary placement for now
	elif request.method == 'POST':
		zipcode = request.form[ 'zipcode' ]
		markets = Market.query.filter_by( market_zip = zipcode )
		return render_template( 'market.html', markets = markets )


@app.route( '/about', methods = [ 'GET' ] )
def about( ):
	return render_template( 'about.html' )


@app.route( '/data', methods = [ 'GET', 'POST' ] )
def data( ):
	if request.method == 'GET':
		return session[ 'zipcode' ]
	elif request.method == 'POST':
		zipcode = request.form[ 'zipcode' ]
		return redirect( url_for( 'zipcode', zipcode = zipcode ) )


@app.route( '/<zipcode>', methods = [ 'GET' ] )
def zipcode( zipcode ):
	session[ 'zipcode' ] = zipcode
	print( 'SESSION ' + session[ 'zipcode' ] )
	print( 'ZIPCODE ' + zipcode )
	digits = re.compile( r'^[0-9]{5}$' )
	if digits.match( zipcode ):
		zipcode = zipcode
		return render_template( 'map.html', zipcode = zipcode )
	else:
		return redirect( '/' )


@app.route( '/json', methods = [ 'POST' ] )
def json( ):
	market = jsonx.loads( request.data.decode( 'utf-8' ) )
	session[ 'market' ] = market
	print( session[ 'market' ] )
	## Build new url to route to by parsing market's name
	url = ''
	print( market[ 'name' ] )
	for char in market[ 'name' ]:
		## Accept only lowercase alphanumeric characters
		if char.isalnum( ):
			if char.isupper( ):
				url += char.lower( )
			else:
				url += char
		## Remove all whitespace and replace with hyphens
		elif char.isspace( ):
			url += '-'
	print( url )
	return jsonx.dumps( market )


@app.route( '/market' )
def market( ):
	return render_template( 'market.html' )


@app.route( '/farm', methods = [ 'GET' ] )
def farmer( ):
	box = [ ]
	farmer = request.args.get( 'farmer' )
	if farmer:
		farmer = Farmer.query.filter_by( first_name = farmer ).first( )
		farpros = FarmerProduct.query.filter_by( farmer_id = farmer.farmer_id ).all( )
		for farpro in farpros:
			category = Category.query.filter_by( category_id = category.category_id ).first( )
			amount.append( category )
		return render_template( 'farm.html', farmer = farmer, farpros = farpros, amount = amount )


@app.route( '/login' )
def login( ):
	return render_template( 'login.html' )

@app.route( '/logout' )
def logout( ):
	return render_template( 'index.html' )

@app.route( '/customer' )
def customer( ):
	return render_template( 'customer.html' )

@app.route( '/farmer-user' )
def farm_user( ):
	return render_template( 'farmer_user.html' )

@app.route( '/recipe' )
def recipe( ):
	return render_template( 'recipe.html' )



if __name__ == '__main__':
	app.run( )


