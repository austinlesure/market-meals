



from app import db
#from datetime import datetime



## Unsure of the exact purpose of this table
''' class FarmerProdcatLink( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'farmer_prodcat_link'
	
	farmer_id = db.Column( db.Integer, db.ForeignKey( 'farmer.farmer_id' ), primary_key = True )
	prodcat_id = db.Column( db.Integer, db.ForeignKey( 'prodcat.prodcat_id' ), primary_key = True ) '''


class Farmer( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'farmers'
	farmer_id = db.Column( db.Integer, primary_key = True )
	## Split off name column into first and last name columns
	''' farmer_name = db.Column( db.String( 255 ) ) '''
	first_name = db.Column( db.String( 255 ) )
	last_name = db.Column( db.String( 255 ) )
	## Potential columns for login and registration authentication
	''' gender = db.Column( db.String( 255 ) )
	birthday = db.Column( db.DateTime )
	email_address = db.Column( db.String( 255 ), unique = True )
	password = db.Column( db.String( 255 ) )
	phone_number = db.Column( db.Integer )
	street_address = db.Column( db.String( 255 ) )
	city = db.Column( db.String( 255 ) )
	state = db.Column( db.String( 2 ) )
	zip_code = zip_code = db.Column( db.Integer ) '''
	
	farm_id = db.Column( db.Integer, db.ForeignKey( 'farms.farm_id' ) )
	
	markets = db.relationship( 'MarketDay', secondary = 'farmer_days', backref = 'farmers' )
	products = db.relationship( 'FarmerProduct', backref = 'farmers' )
	## Temporarily omitted property snce its table is disabled
	''' prodcats = db.relationship( 'Prodcat', secondary = 'farmer_prodcat_link' ) '''
	
	def __init__( self, first_name, last_name ):
		self.farmer_name = first_name + last_name
	
	def __repr__( self ):
		return '<Farmer %r' % self.farmer_name


class FarmerProduct( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'farmer_products'
	## Better to use foreign keys as the primary key here
	''' farmer_product_id = db.Column( db.Integer, primary_key = True ) '''
	farmer_id = db.Column( db.Integer, primary_key = True, db.ForeignKey( 'farmers.farmer_id' ) )
	product_id = db.Column( db.Integer, primary_key = True, db.ForeignKey( 'products.product_id' ) )
	price = db.Column( db.Integer ) ## NOT NULL
	available = db.Column( db.Boolean ) ## NOT NULL
	
	farmers = db.relationship( 'Farmer', backref = 'products' )
	products = db.relationship( 'Product', backref = 'farmers' )
	
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


class Product( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'products'
	product_id = db.Column( db.Integer, primary_key = True )
	product_name = db.Column( db.String( 255 ) ) ## NOT NULL
	
	category_id = db.Column( db.Integer, db.ForeignKey( 'categories.category_id' ) )
	
	markets = db.relationship( 'MarketDay', secondary = 'product_days', backref = 'products' )
	ingredients = db.relationship( 'Ingredient', backref = 'products' )
	farmers = db.relationship( 'FarmerProduct', backref = 'products' )
	
	def __init__( self, product_name, owner_prodcat ):
		self.product_name = product_name
		## Yet to understand its use and purpose in this model
		''' self.owner_prodcat = owner_prodcat '''
	
	def __repr__( self ):
		return '<Product %r' % self.product_name


## Formerly the Prodcat table, as it was ambiguously named
class Category( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'categories'
	category_id = db.Column( db.Integer, primary_key = True )
	category = db.Column( db.String( 255 ) ) ## NOT NULL
	
	products = db.relationship( 'Product', backref = 'categories' )
	## Not sure what relationship this table has with farmers
	''' farmers = db.relationship( 'Farmer', secondary = 'farmer_prodcat_link' ) '''
	
	def __init__( self, category ):
		self.category = category
	
	def __repr__( self ):
		return '<Category %r' % self.category


## Optional table for participating farms at market
class Farm( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'farms'
	farm_id = db.Column( db.Integer, primary_key = True )
	name = db.Column( db.String( 255 ) ) ## NOT NULL
	email_address = db.Column( db.String( 255 ), unique = True )
	phone_number = db.Column( db.Integer )
	street_address = db.Column( db.String( 255 ) ) ## NOT NULL
	city = db.Column( db.String( 255 ) ) ## NOT NULL
	state = db.Column( db.String( 2 ) ) ## NOT NULL
	zip_code = zip_code = db.Column( db.Integer )
	
	farmers = db.relationship( 'Farmer', backref = 'farms' )
	
	def __init__( self, name, email_address, phone_number, street_address, city, state, zip_code ):
		self.name = name
		self.email_address = email_address
		self.phone_number = phone_number
		self.street_address = street_address
		self.city = city
		self.state = state
		self.zip_code = zip_code
	
	def __repr__( self ):
		return 'Farm %r' % self.name


class Market( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'markets'
	market_id = db.Column( db.Integer, primary_key = True )
	name = db.Column( db.String( 255 ) ) ## NOT NULL
	url = db.Column( db.Text, unique = True ) ## NOT NULL
	website = db.Columb( db.Text, unique = True ) ## NOT NULL
	address1 = db.Column( db.String( 255 ) ) ## NOT NULL
	address2 = db.Column( db.String( 255 ) )
	city = db.Column( db.String( 255 ) ) ## NOT NULL
	state = db.Column( db.String( 2 ) ) ## NOT NULL
	zip_code = db.Column( db.Integer ) ## NOT NULL
	
	days = db.relationship( 'MarketDay', backref = 'markets' )
	
	def __init__( self, name, url, website, address1, address2, city, state, zip_code ):
		self.name = name
		self.url = url
		self.website = website
		self.address1 = address1
		self.address2 = address2
		self.city = city
		self.state = state
		self.zip_code = zip_code
	
	def __repr__( self ):
		return '<Market %r' % self.name


class MarketDay( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'market_days'
	market_day_id = db.Column( db.Integer, primary_key = True )
	date = db.Column( db.DateTime ) #, default=datetime.utcnow
	
	market_id = db.Column( db.Integer, db.ForeignKey( 'markets.market_id' ) )
	## Better used in two separate many-to-many tables
	''' farmer_id = db.Column( db.Integer, db.ForeignKey( 'farmers.farmer_id' ) )
	product_id = db.Column( db.Integer, db.ForeignKey( 'products.product_id' ) ) '''
	
	## Implemented through primary key table joins instead
	''' farmerproduct_id = db.relationship( 'FarmerProduct', backref = 'owner_marketday' ) '''
	
	def __init__( self, date ):
		## Unknown uses for the following assigned variables
		''' owner_market, owner_farmer, owner_product '''
		self.date = date
		''' self.owner_market = owner_market
		self.owner_farmer = owner_farmer
		self.owner_product = owner_product '''
	
	def __repr__( self ):
		return '<MarketDay %r' % self.market_day_date


## Farmers' days at market, a many-to-many relationship
farmer_days = db.Table(
	db.Column( 'farmer_id', db.Integer, primary_key = True, db.ForeignKey( 'farmers.farmer_id' ) ),
	db.Column( 'market_day_id', db.Integer, primary_key = True, db.ForeignKey( 'market_days.market_day_id' ) )
)


## A many-to-many table for which day products are sold
product_days = db.Table(
	db.Column( 'product_id', db.Integer, primary_key = True, db.ForeignKey( 'products.product_id' ) ),
	db.Column( 'market_day_id', db.Integer, primary_key = True, db.ForeignKey( 'market_days.market_day_id' ) )
)


class Recipe( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'recipes'
	recipe_id = db.Column( db.Integer, primary_key = True )
	recipe_name = db.Column( db.String( 255 ) ) ## NOT NULL
	## Refactoring into its own normalized, alternative table
	''' recipe_directions = db.Column( db.Text ) '''
	
	ingredients = db.relationship( 'Ingredient', backref = 'recipes' )
	directions = db.relationship( 'Direction', backref = 'recipes' )
	
	def __init__( self, recipe_name, recipe_directions ):
		self.recipe_name = recipe_name
		## Placed into its own table for optimal normalization
		''' self.recipe_directions = recipe_directions '''
	
	def __repr__( self ):
		return '<Recipe %r' % self.recipe_name


## New normalized table for containing recipe directions
class Direction( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'directions'
	direction_id = db.Column( db.Integer, primary_key = True )
	order = db.Column( db.Integer ) ## NOT NULL
	instruction = db.Column( db.Text ) ## NOT NULL
	
	recipe_id = db.Column( db.Integer, db.ForeignKey( 'recipes.recipe_id' ) )
	
	def __init__( self, instruction ):
		self.instruction = instruction
	
	def __repr__( self ):
		return '<Direction %r' % self.instruction


## Was Recipeproduct table, but given more semantic naming
class Ingredient( db.Model ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'ingredients'
	ingredient_id = db.Column( db.Integer, primary_key = True )
	ingredient_quantity = db.Column( db.String( 255 ) )
	
	recipe_id = db.Column( db.Integer, db.ForeignKey( 'recipes.recipe_id' ) )
	product_id = db.Column( db.Integer, db.ForeignKey( 'products.product_id' ) )
	
	def __init__( self, ingredient_quantity, owner_recipe, owner_product ):
		self.ingredient_quantity = ingredient_quantity
		self.owner_recipe = owner_recipe
		self.owner_product = owner_product
	
	def __repr__( self ):
		return '<Ingredient %r' % self.ingredient_quantity



