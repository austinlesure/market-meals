



from marketmeals import app, db
from flask import render_template



@app.route( '/login' )
def login( ):
	return render_template( 'login.html' )


@app.route( '/logout' )
def logout( ):
	return render_template( 'index.html' )


@app.route( '/customer' )
def customer( ):
	return render_template( 'customer.html' )


@app.route( '/recipe' )
def recipe( ):
	return render_template( 'recipe.html' )


""" def get_farmers( ):
	return Farmer.query.filter_by( ).all( )

def get_markets( ):
	return Market.query.filter_by( ).all( )

def get_recipes( ):
	return Recipe.query.filter_by( ).all( )

def get_categories( ):
	return Category.query.filter_by( ).all( )

def get_farmer_products( ):
	return FarmerProduct.query.filter_by( ).all( )

def get_products( ):
	return Product.query.filter_by( ).all( ) """



