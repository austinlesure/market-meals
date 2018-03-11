



import re
from marketmeals.home.utils import html
from flask import Blueprint, render_template, redirect, url_for



home = Blueprint( 'home', __name__, template_folder = html )



@home.route( '/', methods = [ 'GET' ] )
def index( ):
	return render_template( 'home/index.html' )
	
	## Unused method, but temporary placement for now
	''' if request.method == 'GET':
		return render_template( 'index.html' )
	elif request.method == 'POST':
		zipcode = request.form[ 'zipcode' ]
		markets = Market.query.filter_by( market_zip = zipcode )
		return render_template( 'market.html', markets = markets ) '''


@home.route( '/about', methods = [ 'GET' ] )
def about( ):
	return render_template( 'home/about.html' )


## Depreciated for the time being and may be removed
@home.route( '/wild', methods = [ 'GET' ] )
def wild( wild ):
	print( 'Arrived at Wild!' )
	print( wild )
	if re.match( r'^[0-9]{5}$', wild ):
		print( 'Zipcode!' )
		return redirect( url_for( 'geoapi.zipcode', zipcode = wild ) )
	elif re.match( r'^([a-z]+-)*(market){1}(-[a-z]+)*$', wild ):
		print( 'Market!' )
		return redirect( url_for( 'location.market', market = wild ) )
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


@home.route( '/error' )
def error( ):
	return render_template( 'home/error.html' )



