



from flask import Blueprint, request
from models import Farmer
from app import db



## Setup blueprint for data module to enable route access
data = Blueprint( 'data', __name__ )


@data.route( '/get', methods = [ 'GET' ] )
def get( ):
	data = 'Python'
	print( data )
	return data

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



