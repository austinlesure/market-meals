



import re
from marketmeals.index.utils import html
from flask import Blueprint, render_template, redirect, url_for



index = Blueprint( 'index', __name__, template_folder = html )



@index.route( '/', methods = [ 'GET' ] )
def land( ):
	return render_template( 'index/index.html' )
	
	## Unused method, but temporary placement for now
	''' if request.method == 'GET':
		return render_template( 'index.html' )
	elif request.method == 'POST':
		zipcode = request.form[ 'zipcode' ]
		markets = Market.query.filter_by( market_zip = zipcode )
		return render_template( 'market.html', markets = markets ) '''


@index.route( '/about', methods = [ 'GET' ] )
def about( ):
	return render_template( 'index/about.html' )


@index.route( '/error' )
def error( ):
	return render_template( 'index/error.html' )


