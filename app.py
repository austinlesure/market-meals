



import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from data import data



app = Flask( __name__ )
## Modularize app by registering blueprints
app.register_blueprint( data )

db = SQLAlchemy( app )

app.config[ 'DEBUG' ] = True
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = os.environ.get(
	'DATABASE_URL',
	'mysql+pymysql://market-meals:market-meals@localhost:8889/market-meals'
)
app.config[ 'SQLALCHEMY_ECHO' ] = True

app.secret_key = 'MarKetMeaLSiSAMAzinG'



