import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager    
from flask_mail import Mail

app = Flask(__name__)

# secret key for users to stay logged in
app.config['SECRET_KEY'] = '348943509rf4j09w09809cv987v987b'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# config database with sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideas.db'
db = SQLAlchemy(app)
 
#confit login and pw hass
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
bcrypt = Bcrypt(app)

# config email service for PW reset
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

# noQA
from ideas import routes
