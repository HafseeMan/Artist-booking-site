#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

from enum import unique
import json
import sys
import dateutil.parser
import babel
from flask import Flask, jsonify, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask_wtf.csrf import CSRFProtect,  CSRFError


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

#To create local postgresql database connection
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Enable CSRF protection globally for a Flask app.
csrf = CSRFProtect(app)

# (*) TODO: connect to a local postgresql database
migrate = Migrate(app, db) #Initializing migrate


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    shows = db.relationship("Show", backref="venues", lazy=False, cascade="all, delete-orphan")
    past_shows_count = db.Column(db.Integer)
    upcoming_shows_count = db.Column(db.Integer)

    def __repr__(self):
        return f"<Venue id={self.id} name={self.name} city={self.city} state={self.city} address={self.address} phone={self.phone} genres={self.genres} facebook_link={self.facebook_link} website={self.website} seeking_talent={self.seeking_talent} seeking_description={self.seeking_description}> \n"

    # (*) TODO: implement any missing fields, as a database migration using Flask-Migrate


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    genres = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    image_link = db.Column(db.String(500), nullable=False)
    shows = db.relationship("Show", backref="artists", lazy=False, cascade="all, delete-orphan")   
    db.UniqueConstraint('name', name='uix_1')

    # (*) TODO: implement any missing fields, as a database migration using Flask-Migrate
"""  
    def __repr__(self):
        return f"<Artist id={self.id} name={self.name} genres={self.genres} city={self.city} state={self.city} phone={self.phone} website={self.address} facebook_link={self.facebook_link} seeking_description={self.seeking_description} image_link={self.image_link}> \n"
   """  
# (*) TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = "show"

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Show id={self.id} artist_id={self.artist_id} venue_id={self.venue_id} artist_image_link={self.artist_image_link} start_time={self.start_time}> \n"

