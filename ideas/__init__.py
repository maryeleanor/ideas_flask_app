 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 

app = Flask(__name__)

# secret key for users to stay logged in
app.config['SECRET_KEY'] = '348943509rf4j09w09809cv987v987b'

# config database with sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 
   
from ideas import routes
