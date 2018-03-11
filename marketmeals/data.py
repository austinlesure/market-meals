



from marketmeals import db
from marketmeals.models import Farmer
from flask import Blueprint, jsonify



data = Blueprint( 'data', __name__ )



@data.route( '/query', methods = [ 'GET' ] )
def query( ):
	## Try a full database query of farmers
	query = Farmer.query.all( )
	farmers = [ ]
	for item in query:
		farmer = {  }
		for data in dir( item ):
			## Only grab table data from query
			if not hasattr( super( Farmer, item ), data ) and data[ 0 ].isalpha( ):
				farmer[ data ] = getattr( item, data )
		farmers.append( farmer )
	return jsonify( farmers )


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



