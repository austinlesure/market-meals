



from app import app, db
from flask import render_template, redirect, url_for, request, session, flash
from models import Farmer, Product, Prodcat, Market, Marketday, Recipe, Recipeproduct
from hashutils import check_pw_hash



@app.route( '/', methods = [ 'GET', 'POST' ] )
def index( ):
	return render_template( 'index.html' )

@app.route( '/about', methods = [ 'GET' ] )
def about( ):
	return render_template( 'about.html' )
	
@app.route( '/data', methods = [ 'GET', 'POST' ] )
def data( ):
	if request.method == 'GET':
		return session[ 'zipcode' ]
	elif request.method == 'POST':
		zipcode = request.form[ 'zipcode' ]
		session[ 'zipcode' ] = zipcode
		return redirect( url_for( 'zipcode', zipcode = zipcode ) )

@app.route( '/<zipcode>', methods = [ 'GET' ] )
def zipcode( zipcode ):
	zipcode = zipcode
	return render_template( 'map.html', zipcode = zipcode )

@app.route( '/login' )
def login( ):
	return render_template( 'login.html' )

@app.route( '/logout' )
def logout( ):
	return render_template( 'index.html' )

@app.route( '/customer' )
def customer( ):
	return render_template( 'customer.html' )

@app.route( '/farmer-user' )
def farm_user( ):
	return render_template( 'farmer_user.html' )

@app.route( '/farm' )
def farmer( ):
	return render_template( 'farm.html' )

@app.route( '/market' )
def market( ):
	return render_template( 'market.html' )

@app.route( '/recipe' )
def recipe( ):
	return render_template( 'recipe.html' )

if __name__ == '__main__':
	app.run( )


