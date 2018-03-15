from flask import render_template, session, flash, request, redirect
from app import app, db
from models import Farmer, Product, Prodcat, Market, Marketday, Recipe, Recipeproduct, FarmerProductLink, FarmerMarketLink
from hashutils import check_pw_hash

def get_prodcats():
    return Prodcat.query.filter_by().all()

def get_farmer_product_links():
    return FarmerProductLink.query.filter_by().all()

def get_recipe_products():
    return Recipeproduct.query.filter_by().all()

def get_recipes():
    return Recipe.query.filter_by().all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        markets = []
        for market in Market.query.filter_by().all():
            markets.append([market.market_name, market.market_address1 + ", " + market.market_city + ", " + market.market_state + " " + market.market_zip])
        return render_template('index.html', markets=markets)
    elif request.method == 'POST':
        zipcode = request.form['zipcode']
        markets = Market.query.filter_by(market_zip=zipcode)
        return render_template('map.html', markets=markets)

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
        return render_template('farm.html', farmer=farmer, product_list=product_list, prodcats=get_prodcats())
    else:
        return redirect("/")

@app.route('/market', methods=['GET'])
def market():
    farmer_list = []
    recipes = []
    dic = {}

    market = request.args.get('market')
    if market:
        market = Market.query.filter_by(market_name=market).first()
        farmersId = FarmerMarketLink.query.filter_by(market_id=market.market_id).all()
        for farmerId in farmersId:
            farmer = Farmer.query.filter_by(farmer_id=farmerId.farmer_id).first()
            x = farmer.farmer_id
            farmer_list.append(farmer)
            productsId = FarmerProductLink.query.filter_by(farmer_id=farmer.farmer_id).all()
            for productId in productsId:
                product = Product.query.filter_by(product_id=productId.product_id).first()
                for recipe_product in get_recipe_products():
                    if recipe_product.product_id == product.product_id:
                        if recipe_product not in recipes:
                            recipes.append(Recipe.query.filter_by(recipe_id=recipe_product.recipe_id).first())
                if x in dic:
                    # append the new number to the existing array at this slot
                    dic[x].append(product)
                else:
                    # create a new array in this slot
                    dic[x] = [product]
        return render_template('market.html', market=market, farmer_list=farmer_list, prodcats=get_prodcats(), dic=dic,
                               recipes=recipes)
    else:
        return redirect("/")

@app.route('/recipe')
def recipe():
    recipe = request.args.get('recipe')
    if recipe:
        recipe = Recipe.query.filter_by(recipe_name=recipe).first()
        return render_template('recipe.html', recipe=recipe)
    else:
        return render_template('recipe.html', recipes=get_recipes())


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
@app.route('/farm')
def farmer():
    return render_template('farm.html')
@app.route('/market')
def market():
    return render_template('market.html')
@app.route('/map')
def map():
    return render_template('map.html')
'''