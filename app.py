from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from config import database_connection_uri

app = Flask(__name__)

app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = database_connection_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(contacts)