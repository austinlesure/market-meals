



import re
from marketmeals.geoapi.utils import path, html, static
from flask import Blueprint, request, render_template, redirect, url_for, session



geoapi = Blueprint( 'geoapi', __name__, static_url_path = path, static_folder = static, template_folder = html )



@geoapi.route( '/area', methods = [ 'GET', 'POST' ] )
def area( ):
	if request.method == 'GET':
		return session[ 'zipcode' ]
	elif request.method == 'POST':
		session[ 'zipcode' ] = request.form[ 'zipcode' ]
		return redirect( url_for( 'geoapi.zipcode', zipcode = session[ 'zipcode' ] ) )
	else:
		return redirect( '/' )


@geoapi.route( '/<zipcode>', methods = [ 'GET' ] )
def zipcode( zipcode ):
	print( 'Arrived at Zipcode!' )
	digits = re.compile( r'^[0-9]{5}$' )
	if digits.match( zipcode ):
		session[ 'zipcode' ] = zipcode
		print( 'SESSION ' + session[ 'zipcode' ] )
		print( 'ZIPCODE ' + zipcode )
		return render_template( 'geoapi/map.html', zipcode = zipcode )
	else:
		return redirect( '/' )



