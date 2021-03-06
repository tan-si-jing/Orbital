from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(100),nullable=False)
    itineraries = db.relationship('Itinerary', backref=db.backref('crt', lazy='joined'), lazy=True)

class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    #cities = db.relationship('Cities_Itin', lazy='subquery', backref=db.backref('itineraries', lazy=True))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    items = db.relationship('Itinerary_Items', backref='itnry', lazy=True)

class Shared_Permission(db.Model):
    itnry_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    edit = db.Column(db.Boolean)
    itnry = db.relationship('Itinerary', backref='perm', lazy=True)
    user = db.relationship('User', backref='perm', lazy=True)

class Itinerary_Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    itnry_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Integer, nullable=False)
    long = db.Column(db.Integer, nullable=False)
#    __table_args__ = (db.ForeignKeyConstraint(['lat', 'long'], ['location.lat', 'location.long']),)
    date = db.Column(db.String(100), nullable=False)
    time = db.Column(db.Time)
    comments = db.Column(db.String(100))
    position = db.Column(db.Integer, nullable=False)

#class Location(db.Model):
#    name = db.Column(db.String(100), nullable=False)
#    lat = db.Column(db.Integer, primary_key=True)
#    long = db.Column(db.Integer, primary_key=True)
#    items = db.relationship('Itinerary_Items', backref='place', lazy=True)
