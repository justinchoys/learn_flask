from flask import Flask

#app here is name of Flask object
app = Flask(__name__)

#import routes file from app folder
from app import routes