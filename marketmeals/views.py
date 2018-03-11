



import re
from marketmeals import app, db
from marketmeals.models import Farmer, Market, Category, FarmerProduct
from flask import request, render_template, redirect, url_for, session



@app.route( '/', methods = [ 'GET' ] )
def index( ):
	return render_template( 'index.html' )
	
	## Unused method, but temporary placement for now
	''' if request.method == 'GET':
		return render_template( 'index.html' )
	elif request.method == 'POST':
		zipcode = request.form[ 'zipcode' ]
		markets = Market.query.filter_by( market_zip = zipcode )
		return render_template( 'market.html', markets = markets ) '''


@app.route( '/about', methods = [ 'GET' ] )
def about( ):
	return render_template( 'about.html' )


@app.route( '/wild', methods = [ 'GET' ] )
def wild( wild ):
	print( 'Arrived at Wild!' )
	print( wild )
	if re.match( r'^[0-9]{5}$', wild ):
		print( 'Zipcode!' )
		return redirect( url_for( 'code.zipcode', zipcode = wild ) )
	elif re.match( r'^([a-z]+-)*(market){1}(-[a-z]+)*$', wild ):
		print( 'Market!' )
		return redirect( url_for( 'farm.market', market = wild ) )
	return 'Error!'
	
	""" print( 'Arrived at Wild!' )
	print( wild )
	print( re.match( 'market', wild ) )
	print( None )
	if re.match( r'^[0-9]{5}$', wild ):
		print( 'Zipcode!' )
		return redirect( url_for( 'code.zipcode', zipcode = wild ) )
	elif re.match( 'market', wild ):
		print( 'Market! ')
		return redirect( url_for( 'market', market = wild ) )
	else:
		return redirect( '/' ) """


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


@app.route( '/error' )
def error( ):
	return 'Bad route!'



