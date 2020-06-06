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
    itn = Shared_Permission.query.filter_by(user_id=current_user.id).all()
    return render_template('collection.html', itineraries=itn)

@main.route('/view/<int:itnum>', methods=['GET'])
@login_required
def view(itnum):
    view = Shared_Permission.query.filter(and_(user_id==current_user.user_id, itinerary_id==itnum)).first()
    if view:
        itn = Itinerary_Items.query.filter_by(itnry_id=itnum).all()
        render_template('view.html', itn_items=itn)
    else:
        render_template('error.html', message="You do not have permission to view this itinerary")

@main.route('/edit/<int:itnum>')
@login_required
def edit(itnum):
    edit = Shared_Permission.query.filter(and_(user_id==current_user.user_id, itinerary_id==itnum, edit==True)).first()
    if edit:
        itn = Itinerary_Items.query.filter_by(itnry_id=itnum).all()
        render_template('edit.html', itn_items=itn)
    else:
        render_template('error.html', message="You do not have permission to edit this itinerary")
