from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#app here is name of Flask object
app = Flask(__name__)
app.config.from_object(Config)

#setup database instance and database migration engine instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#import routes file from app folder
from app import routes, models