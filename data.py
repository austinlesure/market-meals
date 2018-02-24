



from flask import Blueprint, request



## Setup blueprint for data module to enable route access
data = Blueprint( 'data', __name__ )


@data.route( '/core' )
def core( ):
	snek = 'SNEK!!!'
	print( 'From Python' )
	return snek


