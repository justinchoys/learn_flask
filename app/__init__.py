from flask import Flask
from config import Config

#app here is name of Flask object
app = Flask(__name__)
app.config.from_object(Config)

#import routes file from app folder
from app import routes