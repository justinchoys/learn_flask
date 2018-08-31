import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #Flask-SQLAlchemy extension takes location of application's database from
    #SQLALCHEMY_DATABASE_URI configuration variable

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    #disable unneeded feature of Flask-SQLAlchemy (signal app every time a change is about to be made in database)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    