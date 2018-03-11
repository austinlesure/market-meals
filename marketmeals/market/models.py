



import enum
from marketmeals import db
from marketmeals.index.utils import get_now
from marketmeals.index.models import Base
from sqlalchemy.dialects import postgresql



class Day( enum.Enum ):
	sunday = 'Sunday'
	monday = 'Monday'
	tuesday = 'Tuesday'
	wednesday = 'Wednesday'
	thursday = 'Thursday'
	friday = 'Friday'
	saturday = 'Saturday'


class Market( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'markets'
	market_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	name = db.Column( db.String( 75 ), nullable = False )
	url = db.Column( db.Text, nullable = False, unique = True )
	website = db.Column( db.Text, unique = True )
	email_address = db.Column( db.String( 75 ), unique = True )
	phone_number = db.Column( db.String( 20 ) )
	address_1 = db.Column( db.Text ) ## NOT NULL
	address_2 = db.Column( db.Text )
	city = db.Column( db.String( 40 ), nullable = False )
	state = db.Column( db.String( 2 ), nullable = False )
	zip_code = db.Column( db.Integer, nullable = False )
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
	days = db.relationship( 'MarketDay', backref = 'markets' )
	
	def __init__( self, name, url, address_1,  city, state, zip_code ):
		''' website, email_address, phone_number, address_2, '''
		self.name = name
		self.url = url
		''' self.website = website
		self.email_address = email_address
		self.phone_number = phone_number '''
		self.address_1 = address_1
		''' self.address_2 = address_2 '''
		self.city = city
		self.state = state
		self.zip_code = zip_code
	
	def __repr__( self ):
		return '<Market %r' % self.name


class MarketDay( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'market_days'
	market_day_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	date = db.Column( db.Date ) ## NOT NULL
	day = db.Column( postgresql.ENUM( Day ) ) ## NOT NULL
	opens = db.Column( db.Time( timezone = True ) ) ## NOT NULL
	closes = db.Column( db.Time( timezone = True ) ) ## NOT NULL
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
	market_id = db.Column( db.Integer, db.ForeignKey( 'markets.market_id' ) )
	## Better used in two separate many-to-many tables
	''' farmer_id = db.Column( db.Integer, db.ForeignKey( 'farmers.farmer_id' ) )
	product_id = db.Column( db.Integer, db.ForeignKey( 'products.product_id' ) ) '''
	
	## Implemented through primary key table joins instead
	''' farmerproduct_id = db.relationship( 'FarmerProduct', backref = 'owner_marketday' ) '''
	
	def __init__( self, date, day, opens, closes ):
		## Unknown uses for the following assigned variables
		''' owner_market, owner_farmer, owner_product '''
		self.date = date
		self.day = day
		self.opens = opens
		self.closes = closes
		''' self.owner_market = owner_market
		self.owner_farmer = owner_farmer
		self.owner_product = owner_product '''
	
	def __repr__( self ):
		return '<MarketDay %r' % self.market_day_date



