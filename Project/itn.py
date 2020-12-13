from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, jsonify
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from .models import *
from . import db
import json

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

@itn.route('/newItem', methods=['POST'])
@login_required
def newItem():
    name = request.form['name']
    itnry_id = request.form['itnry_id']
    location = request.form['location']
    lat = request.form['lat']
    long = request.form['long']
    date = request.form['date']
    time = request.form['time']
    comments = request.form['comments']
    position = request.form['position']
    new_item = Itinerary_Items(name=name, itnry_id=itnry_id, location=location, lat=lat, long=long, date=date, time=time, comments=comments, position=position)
    db.session.add(new_item)
    db.session.commit()
    return jsonify(id=new_item.id)

@itn.route('/reorder', methods=['POST'])
@login_required
def reorder():
    pos = request.form['pos']
    pos = json.loads(pos)
    for i in pos:
        id = i[0]
        item = Itinerary_Items.query.get(int(id))
        item.position = i[1]
    db.session.commit()
    return jsonify(pos=pos)

@itn.route('/otherList', methods=['POST'])
@login_required
def otherList():
    id = request.form['id']
    date = request.form['date']
    item = Itinerary_Items.query.get(id)
    item.date = date
    db.session.commit()
    return jsonify(id=id)

@itn.route('/view/<int:itnum>', methods=['GET'])
@login_required
def view(itnum):
    view = Shared_Permission.query.filter((Shared_Permission.user_id==current_user.id) & (Shared_Permission.itnry_id==itnum)).first()
    itn = Itinerary.query.get(itnum)
    owner = (current_user.id == itn.creator)
    if view or owner:
        return render_template('view.html', itn=itn)
    return render_template('error.html', message="You do not have permission to view this itinerary")

@itn.route('/edit/<int:itnum>')
@login_required
def edit(itnum):
    edit = Shared_Permission.query.filter((Shared_Permission.user_id==current_user.id) & (Shared_Permission.itnry_id==itnum) & (Shared_Permission.edit==True)).first()
    itn = Itinerary.query.get(itnum)
    owner = (current_user.id == itn.creator)
    if edit or owner:
        return render_template('edit.html', itn=itn)
    return render_template('error.html', message="You do not have permission to view this itinerary")

@itn.route('/items/<int:itnum>', methods=['GET'])
@login_required
def items(itnum):
    itn_items = Itinerary_Items.query.filter_by(itnry_id=itnum).order_by(Itinerary_Items.position).all()
    all_items = [{'id':i.id,'name':i.name,'itnry_id':i.itnry_id, 'location':i.location, 'lat':i.lat, 'long':i.long, 'date':i.date, 'time':str(i.time), 'comments':i.comments, 'position':i.position} for i in itn_items]
    return jsonify(all_items)

@itn.route('/share_edit', methods=['POST'])
@login_required
def share_edit():
    email = request.form['email']
    perm = request.form['perm']
    itnum = request.form['itnum']
    user = User.query.filter_by(email=email).first()
    exists = Shared_Permission.query.filter(Shared_Permission.user_id==user.id, Shared_Permission.itnry_id==itnum).first()
    if exists:
        db.session.delete(exists)
        db.session.commit()
    new = Shared_Permission(itnry_id=itnum, user_id=user.id, edit=True)
    db.session.add(new)
    db.session.commit()
    return redirect(url_for('itn.edit', itnum=itnum))

@itn.route('/share_view', methods=['POST'])
@login_required
def share_view():
    email = request.form['email']
    perm = request.form['perm']
    itnum = request.form['itnum']
    user = User.query.filter_by(email=email).first()
    exists = Shared_Permission.query.filter(Shared_Permission.user_id==user.id, Shared_Permission.itnry_id==itnum).first()
    if exists:
        db.session.delete(exists)
        db.session.commit()
    new = Shared_Permission(itnry_id=itnum, user_id=user.id, edit=False)
    db.session.add(new)
    db.session.commit()
    return redirect(url_for('itn.edit', itnum=itnum))

@itn.route('/sort', methods=['POST'])
@login_required
def sort():
    gbtb = Itinerary_Items.query.get(3)
    sgz = Itinerary_Items.query.get(4)
    nus = Itinerary_Items.query.get(2)
    cap = Itinerary_Items.query.get(1)
    gbtb.position = 3
    sgz.position = 2
    nus.position = 1
    cap.position = 4
    db.session.commit()
    return redirect(url_for('itn.edit', itnum=3))
