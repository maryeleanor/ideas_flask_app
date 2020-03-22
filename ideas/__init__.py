import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# secret key for users to stay logged in
app.config['SECRET_KEY'] = '348943509rf4j09w09809cv987v987b'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# config database with sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideas.db'
db = SQLAlchemy(app)

# noQA
from ideas import routes