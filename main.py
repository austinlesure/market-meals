from flask import render_template #session, flash, request, redirect
from app import app #db
#from models import User
#from hashutils import check_pw_hash

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
