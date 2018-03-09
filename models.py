from app import db
#from datetime import datetime

class Farmer(db.Model):
    __table_args__ = {'extend_existing': True}
    farmer_id = db.Column(db.Integer, primary_key=True)
    farmer_name = db.Column(db.String(255))
    marketday_id = db.relationship('Marketday', backref='owner_farmer')

    def __init__(self, farmer_name):
        self.farmer_name = farmer_name

    def __repr__(self):
        return '<Farmer %r' % self.farmer_name

class Product(db.Model):
    __table_args__ = {'extend_existing': True}
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255))
    prodcat_id = db.Column(db.Integer, db.ForeignKey('prodcat.prodcat_id'))
    marketday_id = db.relationship('Marketday', backref='owner_product')
    recipeproduct_id = db.relationship('Recipeproduct', backref='owner_product')

    def __init__(self, product_name, owner_prodcat):
        self.product_name = product_name
        self.owner_prodcat = owner_prodcat

    def __repr__(self):
        return '<Product %r' % self.product_name

class Prodcat(db.Model):
    __table_args__ = {'extend_existing': True}
    prodcat_id = db.Column(db.Integer, primary_key=True)
    prodcat_name = db.Column(db.String(255))
    product = db.relationship('Product', backref='owner_prodcat')

    def __init__(self, prodcat_name):
        self.prodcat_name = prodcat_name

    def __repr__(self):
        return '<Prodcat %r' % self.prodcat_name

class Market(db.Model):
    __table_args__ = {'extend_existing': True}
    market_id = db.Column(db.Integer, primary_key=True)
    market_name = db.Column(db.String(255))
    market_address1 = db.Column(db.String(255))
    market_address2 = db.Column(db.String(255))
    market_city = db.Column(db.String(255))
    market_state = db.Column(db.String(2))
    market_zip = db.Column(db.String(5))
    marketday_id = db.relationship('Marketday', backref='owner_market')

    def __init__(self, market_name, market_address1, market_address2, market_city, market_state, market_zip):
        self.market_name = market_name
        self.market_address1 = market_address1
        self.market_address2 = market_address2
        self.market_city = market_city
        self.market_state = market_state
        self.market_zip = market_zip

    def __repr__(self):
        return '<Market %r' % self.market_name

class Marketday(db.Model):
    __table_args__ = {'extend_existing': True}
    marketday_id = db.Column(db.Integer, primary_key=True)
    marketday_date = db.Column(db.DateTime) #, default=datetime.utcnow
    market_id = db.Column(db.Integer, db.ForeignKey('market.market_id'))
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.farmer_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))

    def __init__(self, marketday_date, owner_market, owner_farmer, owner_product):
        self.marketday_date = marketday_date
        self.owner_market = owner_market
        self.owner_farmer = owner_farmer
        self.owner_product = owner_product

    def __repr__(self):
        return '<Marketday %r' % self.marketday_date

class Recipe(db.Model):
    __table_args__ = {'extend_existing': True}
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255))
    recipe_directions = db.Column(db.Text)
    recipeproduct_id = db.relationship('Recipeproduct', backref='owner_recipe')

    def __init__(self, recipe_name, recipe_directions):
        self.recipe_name = recipe_name
        self.recipe_directions = recipe_directions

    def __repr__(self):
        return '<Recipe %r' % self.recipe_name

class Recipeproduct(db.Model):
    __table_args__ = {'extend_existing': True}
    recipeproduct_id = db.Column(db.Integer, primary_key=True)
    recipeproduct_amount_required = db.Column(db.String(255))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))

    def __init__(self, recipe_product_amount_required, owner_recipe, owner_product):
        self.recipe_product_amount_required = recipe_product_amount_required
        self.owner_recipe = owner_recipe
        self.owner_product = owner_product

    def __repr__(self):
        return '<Recipeproduct %r' % self.recipe_product_amount_required