from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(100),nullable=False)
    itineraries = db.relationship('Itinerary', backref=db.backref('c', lazy='joined'), lazy=True)

class Itinerary(db.Model):
    itnry_id = db.Column(db.Integer, primary_key=True)
    itinry_name = db.Column(db.String(100), nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    cities = db.relationship('Cities_Itin', lazy='subquery', backref=db.backref('itineraries', lazy=True))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

class Shared_Permission(db.Model):
    itnry_id = db.Column(db.Integer, db.ForeignKey('itinerary.itnry_id'), nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    edit = db.Column(db.Boolean)

class Itinerary_Items(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    itnry_id = db.Column(db.Integer, db.ForeignKey('itinerary.itnry_id'), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), db.ForeignKey('city.city_name'), nullable=False)
    date = db.Column(db.Date)
    time = db.Column(db.Time, nullable=False)
    comments = db.Column(db.String(100))
    position = db.Column(db.Integer, nullable=False)

class City(db.Model):
    city_name = db.Column(db.String(100), primary_key=True)
    country = db.Column(db.String(100), nullable=False)

class Cities_Itin(db.Model):
    city = db.Column(db.String(100), db.ForeignKey('city.city_name'), primary_key=True)
    itnry_id = db.Column(db.Integer, db.ForeignKey('itinerary.itnry_id'), primary_key=True)

class Accomodation(db.Model):
    itnry_id = db.Column(db.Integer, db.ForeignKey('itinerary.itnry_id'), primary_key=True)
    date = db.Column(db.Date, nullable=False, primary_key=True)
    morning = db.Column(db.Boolean, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), db.ForeignKey('city.city_name'))

class Sort(db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('itinerary_items.item_id'), primary_key=True)
    index = db.Column(db.Integer)