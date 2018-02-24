



from app import app
from flask import request



## Route won't run from this file yet
@app.route( '/data' )
def data( ):
	snek = 'SNEK!!!'
	print( 'From Python' )
	return snek


