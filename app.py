from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import names
from marketAddress import MarketAddress

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql+pymysql://market-meals:market-meals@localhost:8889/market-meals')
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
app.secret_key = 'MarKetMeaLSiSAMAzinG'

@app.route('/', methods=['GET', 'POST'])
def func():
  if request.method == 'POST':
    zipcode = request.form['zipcode']
    return redirect(url_for('success', name = zipcode) )
  else:
    zipcode = request.args.get('zipcode')
    return redirect(url_for('success', name = zipcode) )
    
@app.route("/google-maps", methods=['GET'])
def func(marketName):
def names():
  result = query_db("SELECT mname FROM market.marketName")
  data = json.dumps(result)
  resp = Response(data, status=200, mimetype='application/json')
  return resp
   


