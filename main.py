from flask import render_template, session, flash, request, redirect
from app import app, db
from models import Farmer, Product, Prodcat, Market, Marketday, Recipe, Recipeproduct, FarmerProductLink, FarmerMarketLink
from hashutils import check_pw_hash

def get_prodcats():
    return Prodcat.query.filter_by().all()

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
    product_list = []
    farmer = request.args.get('farmer')
    if farmer:
        farmer = Farmer.query.filter_by(farmer_name=farmer).first()
        productIds = FarmerProductLink.query.filter_by(farmer_id=farmer.farmer_id).all()
        for productId in productIds:
            product = Product.query.filter_by(product_id=productId.product_id).first()
            product_list.append(product)


            '''
            
            get all prodcats
            for prodcat in prodcats
            see which 
            
            '''



        return render_template('farm.html', farmer=farmer, product_list=product_list, prodcats=get_prodcats())
    else:
        return redirect("/")

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')


if __name__ == '__main__':
    app.run()







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
