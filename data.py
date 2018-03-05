



from flask import Blueprint, request
from models import Farmer
from app import db



## Setup blueprint for data module to enable route access
data = Blueprint( 'data', __name__ )



@data.route( '/post', methods = [ 'POST' ] )
def post( ):
	## Decode encoded data posted from frontend
	data = request.data.decode( 'utf-8' )
	print( data )
	return data


@data.route( '/query', methods = [ 'GET', 'POST' ] )
def query( ):
	## Insert a new database entry
	bob = Farmer( farmer_name = 'Bob' )
	db.session.add( bob )
	db.session.commit( )
	## Query new entry and return it
	data = Farmer.query.filter_by( farmer_name = 'Bob' ).first( )
	return data.farmer_name


def get_farmers( ):
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
	return Product.query.filter_by( ).all( )


