



from marketmeals import db
from sqlalchemy.dialects import postgresql
from datetime import datetime, timezone



## Base class for models to inherit from instead
Base = db.Model



## Unsure of the exact purpose of this table
''' class FarmerProdcatLink( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'farmer_prodcat_link'
	
	farmer_id = db.Column( db.Integer, db.ForeignKey( 'farmer.farmer_id' ), primary_key = True )
	prodcat_id = db.Column( db.Integer, db.ForeignKey( 'prodcat.prodcat_id' ), primary_key = True ) '''


class FarmerProduct( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'farmer_products'
	## Better to use foreign keys as the primary key here
	''' farmer_product_id = db.Column( db.Integer, primary_key = True ) '''
	farmer_id = db.Column( db.Integer, db.ForeignKey( 'farmers.farmer_id' ), primary_key = True )
	product_id = db.Column( db.Integer, db.ForeignKey( 'products.product_id' ), primary_key = True )
	price = db.Column( postgresql.MONEY ) ## NOT NULL
	available = db.Column( db.Boolean ) ## NOT NULL
	
	farmers = db.relationship( 'Farmer', backref = 'wares' )
	products = db.relationship( 'Product', backref = 'vendors' )
	
	## Moved to other many-to-many tables for normalization
	''' market_day_id = db.Column( db.Integer, db.ForeignKey( 'market_days.market_day_id' ) ) '''
	
	def __init__( self, price, available ):
		## Taken out until deeper understanding of use is known
		''' owner_farmer, owner_product, owner_marketday '''
		self.price = price
		self.available = available
		''' self.owner_farmer = owner_farmer
		self.owner_product = owner_product
		self.owner_marketday = owner_marketday '''
	
	def __repr__( self ):
		return '<FarmerProduct %r' % self.available


class Product( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'products'
	product_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	name = db.Column( db.String( 40 ), nullable = False )
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = lambda : datetime.now( timezone.utc ) )
	updated_at = db.Column( db.DateTime( timezone = True ), onupdate = lambda : datetime.now( timezone.utc ) )
	
	category_id = db.Column( db.Integer, db.ForeignKey( 'categories.category_id' ) )
	
	markets = db.relationship( 'MarketDay', secondary = 'product_days', backref = 'products' )
	ingredients = db.relationship( 'Ingredient', backref = 'products' )
	farmers = db.relationship( 'FarmerProduct', backref = 'wares' )
	
	def __init__( self, name ):
		''' owner_prodcat '''
		self.name = name
		## Yet to understand its use and purpose in this model
		''' self.owner_prodcat = owner_prodcat '''
	
	def __repr__( self ):
		return '<Product %r' % self.product_name


## Formerly the Prodcat table, as it was ambiguously named
class Category( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'categories'
	category_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	category = db.Column( db.String( 255 ) )
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = lambda : datetime.now( timezone.utc ) )
	updated_at = db.Column( db.DateTime( timezone = True ), onupdate = lambda : datetime.now( timezone.utc ) )
	
	products = db.relationship( 'Product', backref = 'categories' )
	## Not sure what db.relationship this table has with farmers
	''' farmers = db.relationship( 'Farmer', secondary = 'farmer_prodcat_link' ) '''
	
	def __init__( self, category ):
		self.category = category
	
	def __repr__( self ):
		return '<Category %r' % self.category


## A many-to-many table for which day products are sold
product_days = db.Table( 'product_days', Base.metadata,
	db.Column( 'product_id', db.Integer, db.ForeignKey( 'products.product_id' ), primary_key = True ),
	db.Column( 'market_day_id', db.Integer, db.ForeignKey( 'market_days.market_day_id' ), primary_key = True )
)


class Recipe( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'recipes'
	recipe_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	name = db.Column( db.String( 50 ), nullable = False, unique = True )
	## Refactoring into its own normalized, alternative table
	''' recipe_directions = db.Column( db.Text ) '''
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = lambda : datetime.now( timezone.utc ) )
	updated_at = db.Column( db.DateTime( timezone = True ), onupdate = lambda : datetime.now( timezone.utc ) )
	
	ingredients = db.relationship( 'Ingredient', backref = 'recipes' )
	directions = db.relationship( 'Direction', backref = 'recipes' )
	
	def __init__( self, name, recipe_directions ):
		self.name = name
		## Placed into its own table for optimal normalization
		''' self.recipe_directions = recipe_directions '''
	
	def __repr__( self ):
		return '<Recipe %r' % self.recipe_name


## New normalized table for containing recipe directions
class Direction( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'directions'
	direction_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	order = db.Column( db.SmallInteger ) ## NOT NULL
	summary = db.Column( db.String( 200 ) )
	instruction = db.Column( db.Text ) ## NOT NULL
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = lambda : datetime.now( timezone.utc ) )
	updated_at = db.Column( db.DateTime( timezone = True ), onupdate = lambda : datetime.now( timezone.utc ) )
	
	recipe_id = db.Column( db.Integer, db.ForeignKey( 'recipes.recipe_id' ) )
	
	def __init__( self, order, instruction ):
		self.order = order
		self.instruction = instruction
	
	def __repr__( self ):
		return '<Direction %r' % self.instruction


## Was Recipeproduct table, but given more semantic naming
class Ingredient( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'ingredients'
	ingredient_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	ingredient_quantity = db.Column( db.String( 255 ) )
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = lambda : datetime.now( timezone.utc ) )
	updated_at = db.Column( db.DateTime( timezone = True ), onupdate = lambda : datetime.now( timezone.utc ) )
	
	recipe_id = db.Column( db.Integer, db.ForeignKey( 'recipes.recipe_id' ) )
	product_id = db.Column( db.Integer, db.ForeignKey( 'products.product_id' ) )
	
	def __init__( self, ingredient_quantity ):
		## Old names for previous database model backrefs
		''' owner_recipe, owner_product '''
		self.ingredient_quantity = ingredient_quantity
		''' self.owner_recipe = owner_recipe
		self.owner_product = owner_product '''
	
	def __repr__( self ):
		return '<Ingredient %r' % self.ingredient_quantity



