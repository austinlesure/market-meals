



from marketmeals import app, db
from marketmeals.models import Farmer, Category, FarmerProduct
from flask import request, render_template



@app.route( '/farm', methods = [ 'GET' ] )
def farmer( ):
	box = [ ]
	farmer = request.args.get( 'farmer' )
	if farmer:
		farmer = Farmer.query.filter_by( first_name = farmer ).first( )
		farpros = FarmerProduct.query.filter_by( farmer_id = farmer.farmer_id ).all( )
		for farpro in farpros:
			category = Category.query.filter_by( category_id = category.category_id ).first( )
			amount.append( category )
		return render_template( 'farm.html', farmer = farmer, farpros = farpros, amount = amount )


@app.route( '/login' )
def login( ):
	return render_template( 'login.html' )


@app.route( '/logout' )
def logout( ):
	return render_template( 'index.html' )


@app.route( '/customer' )
def customer( ):
	return render_template( 'customer.html' )


@app.route( '/farmer' )
def farm_user( ):
	return render_template( 'farmer.html' )


@app.route( '/recipe' )
def recipe( ):
	return render_template( 'recipe.html' )



