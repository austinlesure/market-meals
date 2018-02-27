from flask import render_template, session, flash, request, redirect
from app import app, db
from models import Farmer, Product, Prodcat, Market, Marketday, Recipe, Recipeproduct
from hashutils import check_pw_hash

def get_farmers():
    return Farmer.query.filter_by().all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        zipcode = request.form['zipcode']
        markets = Market.query.filter_by(market_zip=zipcode)
        return render_template('market.html', markets=markets)

@app.route('/about')
def about():
    return render_template('about.html')

'''
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('index.html')
'''

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/farmer-user')
def farm_user():
    return render_template('farmer_user.html')

@app.route('/farm')
def farmer():
    return render_template('farm.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

if __name__ == '__main__':
    app.run()
