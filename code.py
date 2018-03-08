



import re
from flask import Blueprint, request, render_template, redirect, url_for, session



code = Blueprint( 'code', __name__ )



@code.route( '/zone', methods = [ 'GET', 'POST' ] )
def zone( ):
	if request.method == 'GET':
		return session[ 'zipcode' ]
	elif request.method == 'POST':
		session[ 'zipcode' ] = request.form[ 'zipcode' ]
		return redirect( url_for( 'code.zipcode', zipcode = session[ 'zipcode' ] ) )
	else:
		return redirect( '/' )


@code.route( '/<zipcode>', methods = [ 'GET' ] )
def zipcode( zipcode ):
	digits = re.compile( r'^[0-9]{5}$' )
	if digits.match( zipcode ):
		session[ 'zipcode' ] = zipcode
		print( 'SESSION ' + session[ 'zipcode' ] )
		print( 'ZIPCODE ' + zipcode )
		return render_template( 'map.html', zipcode = zipcode )
	else:
		return redirect( '/' )



