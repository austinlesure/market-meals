



from flask import Blueprint, request



## Setup blueprint for data module to enable route access
data = Blueprint( 'data', __name__ )


@data.route( '/get', methods = [ 'GET' ] )
def get( ):
	print( 'In the snake cave!' )
	return 'Snake in my script!'

@data.route( '/post', methods = [ 'POST' ] )
def post( ):
	## Decode encoded data posted from frontend
	data = request.data.decode( 'utf-8' )
	print( 'Feed the snake ' + data + '!' )
	return data


