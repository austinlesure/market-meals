



import os
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib import parse



app = Flask( __name__ )
db = SQLAlchemy( app )


## Modularize app by registering blueprints
from marketmeals.portal.views import portal
from marketmeals.code import code
from marketmeals.farm import farm
from marketmeals.data import data
app.register_blueprint( portal )
app.register_blueprint( code )
app.register_blueprint( farm )
app.register_blueprint( data )


## Using psycopg2 to connect to database
parse.uses_netloc.append( 'postgres' )
url = parse.urlparse( os.environ[ 'DATABASE_URL' ] )

conn = psycopg2.connect(
	database = url.path[ 1: ],
	user = url.username,
	password = url.password,
	host = url.hostname,
	port = url.port
)


app.config[ 'DEBUG' ] = True
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = os.environ[ 'DATABASE_URL' ]
## Omitted placeholder database access data
''' app.config[ 'SQLALCHEMY_DATABASE_URI' ] = os.environ.get(
	'DATABASE_URL',
	'postgresql+psycopg2://' + 'user' + ':' + 'password' + '@' + 'host' + ':' + 'port' + '/' + 'dbname'
) '''
app.config[ 'SQLALCHEMY_ECHO' ] = False


## This is a security risk and should be moved
app.secret_key = 'MarKetMeaLSiSAMAzinG'



import marketmeals.views



