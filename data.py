



from flask import Blueprint



## Setup blueprint for data module to enable route access
data = Blueprint( 'data', __name__ )


@data.route( '/get', methods = [ 'GET' ] )
def get( ):
	print( 'In the snake cave!' )
	return 'Snake in my script!'

@data.route( '/post', methods = [ 'POST' ] )
def post( input = None ):
	item = input
	print( 'Feed the snake!' )
	print( item )
	return item


