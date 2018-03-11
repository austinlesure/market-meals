



from app import db
from flask import Blueprint
from models import Farmer



data = Blueprint( 'data', __name__ )



@data.route( '/query', methods = [ 'POST' ] )
def query( ):
	## Try a full database query of farmers
	farmers = Farmer.query.all( )
	for farmer in farmers:
		print( farmer )
	return 'Hah'


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



