from flask import render_template, session, flash, request, redirect
from app import app, db
from models import Farmer, Product, Prodcat, Market, Marketday, Recipe, Recipeproduct, FarmerProdcatLink
from hashutils import check_pw_hash

def get_farmers():
    return Farmer.query.filter_by().all()

def get_markets():
    return Market.query.filter_by().all()

def get_recipes():
    return Recipe.query.filter_by().all()

def get_prodcats():
    return Prodcat.query.filter_by().all()

def get_farmer_prodcat_link():
    return FarmerProdcatLink.query.filter_by().all()

def get_products():
    return Product.query.filter_by().all()

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

@app.route('/farm', methods=['GET'])
def farmer():
    prodcat_list = []
    farmer = request.args.get('farmer')
    if farmer:
        farmer = Farmer.query.filter_by(farmer_name=farmer).first()
        prodcatsId = FarmerProdcatLink.query.filter_by(farmer_id=farmer.farmer_id).all()
        for prodcatId in prodcatsId:
            prodcat = Prodcat.query.filter_by(prodcat_id=prodcatId.prodcat_id).first()
            prodcat_list.append(prodcat)
        return render_template('farm.html', farmer=farmer, prodcatsId=prodcatsId, prodcat_list=prodcat_list)

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

'''
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/farmer-user')
def farm_user():
    return render_template('farmer_user.html')
    
@app.route('/map')
def map():
    return render_template('map.html')
'''

if __name__ == '__main__':
    app.run()
