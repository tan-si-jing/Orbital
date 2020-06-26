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
    items = db.relationship('Itinerary_Items', backref='itin', lazy=True)

class Shared_Permission(db.Model):
    itnry_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    edit = db.Column(db.Boolean)

class Itinerary_Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    itnry_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    #city = db.Column(db.String(100), db.ForeignKey('cities_itin.city'), nullable=False)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    comments = db.Column(db.String(100))
    position = db.Column(db.Integer, nullable=False)

#class Cities_Itin(db.Model):
#    city = db.Column(db.String(100), primary_key=True)
#    country = db.Column(db.String(100), primary_key=True)
#    itnry_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), primary_key=True)

#class Accomodation(db.Model):
#    itnry_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), primary_key=True)
#    date = db.Column(db.Date, nullable=False, primary_key=True)
#    morning = db.Column(db.Boolean, primary_key=True)
#    location = db.Column(db.String(100), nullable=False)
#    city = db.Column(db.String(100))

#class Sort(db.Model):
#    item_id = db.Column(db.Integer, db.ForeignKey('itinerary_items.id'), primary_key=True)
#    index = db.Column(db.Integer)
