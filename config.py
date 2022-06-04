import os
    
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://hafsah:1234@localhost:5432/flask_db'
##dialect-username-password-host-port-dbName

SQLALCHEMY_TRACK_MODIFICATIONS = False
