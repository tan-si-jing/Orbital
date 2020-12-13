from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from .models import *
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home')
@login_required
def home():
    # We need all the account info for the user so we can display it on the profile page
    account = current_user
    # Show the profile page with account info
    return render_template('home.html', account=account)

@main.route('/itineraries') #show both shared with me and my own
@login_required
def collection():
    mine = Itinerary.query.filter_by(creator=current_user.id).all()
    itn = Shared_Permission.query.filter_by(user_id=current_user.id).all()
    shared = Itinerary.query.get(3)
    return render_template('collections.html', mine=mine, shared=shared)
