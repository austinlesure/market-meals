



from flask import Blueprint, request



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



