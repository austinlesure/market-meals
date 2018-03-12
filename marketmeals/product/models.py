



from marketmeals import db
from marketmeals.index.utils import get_now
from marketmeals.index.models import Base
from marketmeals.recipe.models import Ingredient
from sqlalchemy.dialects import postgresql



class Product( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'products'
	product_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	name = db.Column( db.String( 40 ), nullable = False )
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
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


## Formerly the Prodcat table, as it was ambiguously named
class Category( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'categories'
	category_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	category = db.Column( db.String( 255 ) )
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
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



