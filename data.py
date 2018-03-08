



import json
from app import db
from flask import Flask, Blueprint, request
from models import Farmer



## Setup blueprint for data module to enable route access
data = Blueprint( 'data', __name__ )



@data.route( '/json', methods = [ 'POST' ] )
def post( ):
	## View initial request json data as bytes type
	data = request.data
	print( type( request.data ) )
	## Decode encoded data posted from frontend
	data = request.data.decode( 'utf-8' )
	print( type( data ) )
	## Transform json string into operable dictionary
	data = json.loads( data )
	print( type( data ) )
	## Give back data reverted into json response
	return json.dumps( data )


@data.route( '/query', methods = [ 'GET', 'POST' ] )
def query( ):
	## Insert a new database entry
	bob = Farmer( first_name = 'Bob', last_name = 'Bobbson' )
	db.session.add( bob )
	db.session.commit( )
	## Query new entry and return it
	data = db.session.query( Farmer ).filter_by( first_name = 'Bob' ).first( )
	return data.first_name


''' def get_farmers( ):
	return Farmer.query.filter_by( ).all( )

def get_markets( ):
	return Market.query.filter_by( ).all( )

def get_recipes( ):
	return Recipe.query.filter_by( ).all( )

def get_prodcats( ):
	return Prodcat.query.filter_by( ).all( )

def get_farmer_prodcat_link( ):
	return FarmerProdcatLink.query.filter_by( ).all( )

def get_products( ):
	return Product.query.filter_by( ).all( ) '''


