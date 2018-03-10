



import json
from app import db
from farm import farm
from flask import Blueprint, request, session
from models import Market



data = Blueprint( 'data', __name__ )



@data.route( '/query', methods = [ 'POST' ] )
def query( ):
	## Insert a new database entry
	bob = Farmer( first_name = 'Bob', last_name = 'Bobbson' )
	db.session.add( bob )
	db.session.commit( )
	## Query new entry and return it
	data = db.session.query( Farmer ).filter_by( first_name = 'Bob' ).first( )
	return json.dumps( session[ 'volume' ] )


""" def get_farmers( ):
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
	return Product.query.filter_by( ).all( ) """



