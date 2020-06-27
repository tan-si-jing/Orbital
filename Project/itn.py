from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, jsonify
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from .models import *
from . import db

itn = Blueprint('itn', __name__)

@itn.route('/newItn', methods=['POST'])
@login_required
def newItn():
    req = request.get_json()
    name = req['name']
    creator = current_user.id
    country = req['country']
    start_date = req['start_date']
    end_date = req['end_date']
    new_itn = Itinerary(name=name, creator=creator, country=country, start_date=start_date, end_date=end_date)
    db.session.add(new_itn)
    db.session.commit()
    return redirect(url_for('itn.edit', itnum=new_itn.id))

@itn.route('/view/<int:itnum>', methods=['GET'])
@login_required
def view(itnum):
    view = Shared_Permission.query.filter((Shared_Permission.user_id==current_user.id) & (Shared_Permission.itnry_id==itnum)).first()
    itn = Itinerary.query.filter_by(itnry_id=itnum).first()
    owner = current_user.id == itn.creator
    if view or owner:
        itn_items = Itinerary_Items.query.filter_by(itnry_id=itnum).all()
        return render_template('view.html', itn=itn, itn_items=itn_items)
    return render_template('error.html', message="You do not have permission to view this itinerary")

@itn.route('/edit/<int:itnum>')
@login_required
def edit(itnum):
    itn_items = Itinerary_Items.query.filter_by(itnry_id=itnum).all()
    return render_template('edit.html', itn=itn, itn_items=itn_items)
