from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, jsonify
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from .models import *
from . import db

itn = Blueprint('itn', __name__)

@itn.route('/newItn', methods=['POST'])
@login_required
def newItn():
    name = request.form.get('name')
    creator = current_user.id
    country = request.form.get('country')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    new_itn = Itinerary(name=name, creator=creator, country=country, start_date=start_date, end_date=end_date)
    db.session.add(new_itn)
    db.session.commit()
    return redirect(url_for('itn.edit', itnum=new_itn.id))

@itn.route('/view/<int:itnum>', methods=['GET'])
@login_required
def view(itnum):
    view = Shared_Permission.query.filter(user_id==current_user.id, itinerary_id==itnum).first()
    if view:
        itn_items = Itinerary_Items.query.filter_by(itnry_id=itnum).all()
        itn = Itinerary.query.filter_by(itnry_id=itnum).first()
        return render_template('view.html', itn=itn, itn_items=itn_items)
    return render_template('error.html', message="You do not have permission to view this itinerary")

@itn.route('/edit/<int:itnum>')
@login_required
def edit(itnum):
    edit = Shared_Permission.query.filter(user_id==current_user.id, itinerary_id==itnum, edit==True).first()
    if edit:
        itn_items = Itinerary_Items.query.filter_by(itnry_id=itnum).all()
        itn = Itinerary.query.filter_by(itnry_id=itnum).first()
        return render_template('edit.html', itn=itn, itn_items=itn_items)
    return render_template('error.html', message="You do not have permission to edit this itinerary")
