import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/fyyur_db'

"""
dialect = postgresql
user = postgres
password = (no password)
local host
port = 5432

db_name = fyyur_db
"""
