from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Sport, GearItem
app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///sportgear.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# JSON APIs to view gear information
@app.route('/sport/<int:sport_id>/gear/JSON')
def sportGearJSON(sport_id):
    sport = session.query(Sport).filter_by(id=sport_id).one()
    items = session.query(GearItem).filter_by(
        sport_id=sport_id).all()
    return jsonify(GearItems=[i.serialize for i in items])


@app.route('/sport/<int:sport_id>/gear/<int:gear_id>/JSON')
def gearItemJSON(sport_id, gear_id):
    gearItem = session.query(GearItem).filter_by(id=gear_id).one()
    return jsonify(GearItem=gearItem.serialize)


@app.route('/sport/JSON')
def sportsJSON():
    sports = session.query(Sport).all()
    return jsonify(sports=[r.serialize for r in sports])


# Shows all sports
@app.route('/')
@app.route('/sport/')
def showSports():
    sports = session.query(Sport).order_by(asc(Sport.name))
    return render_template('sports.html', sports=sports)


# Create a new sport
@app.route('/sport/new/', methods=['GET', 'POST'])
def newSport():
    if request.method == 'POST':
        newSport = Sport(name=request.form['name'])
        session.add(newSport)
        flash('New Sport %s Successfully Created' % newSport.name)
        session.commit()
        return redirect(url_for('showSports'))
    else:
        return render_template('newSport.html')


# Edit a sport
@app.route('/sport/<int:sport_id>/edit/', methods=['GET', 'POST'])
def editSport(sport_id):
    editedSport = session.query(Sport).filter_by(id=sport_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedSport.name = request.form['name']
        flash('Sport Successfully Edited %s' % editedSport.name)
        return redirect(url_for('showSports'))
    else:
        return render_template('editSport.html', sport=editedSport)


# Delete a sport
@app.route('/sport/<int:sport_id>/delete/', methods=['GET', 'POST'])
def deleteSport(sport_id):
    sportToDelete = session.query(Sport).filter_by(id=sport_id).one()
    if request.method == 'POST':
        session.delete(sportToDelete)
        flash('%s Successfully Deleted' % sportToDelete.name)
        session.commit()
        return redirect(url_for('showSports', sport_id=sport_id))
    else:
        return render_template('deleteSport.html', sport=sportToDelete)


# Show sport gear
@app.route('/sport/<int:sport_id>/')
@app.route('/sport/<int:sport_id>/gear/')
def sportGear(sport_id):
        sport = session.query(Sport).filter_by(id=sport_id).one()
        items = session.query(GearItem).filter_by(sport_id=sport_id).all()
        return render_template('gear.html', items=items, sport=sport)


# Create a new gear item
@app.route('/sport/<int:sport_id>/gear/new/', methods=['GET', 'POST'])
def newGearItem(sport_id):
    sport = session.query(Sport).filter_by(id=sport_id).one()
    if request.method == 'POST':
        newItem = GearItem(
            name=request.form['name'], description=request.form['description'],
            sport_id=sport_id)
        session.add(newItem)
        session.commit()
        flash('New Gear %s Item Successfully Created' % (newItem.name))
        return redirect(url_for('sportGear', sport_id=sport_id))
    else:
        return render_template('newgearitem.html', sport_id=sport_id)


# Edit a gear item
@app.route(
    '/sport/<int:sport_id>/<int:gear_id>/edit/', methods=['GET', 'POST'])
def editGearItem(sport_id, gear_id):
    editedItem = session.query(GearItem).filter_by(id=gear_id).one()
    sport = session.query(Sport).filter_by(id=sport_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        flash("Gear Item has been edited")
        return redirect(url_for('sportGear', sport_id=sport_id))
    else:
        return render_template(
            'editgearitem.html', sport_id=sport_id, gear_id=gear_id,
            item=editedItem)


# Delete a gear item
@app.route(
    '/sport/<int:sport_id>/gear/<int:gear_id>/delete',
    methods=['GET', 'POST'])
def deleteGearItem(sport_id, gear_id):
    sport = session.query(Sport).filter_by(id=sport_id).one()
    itemToDelete = session.query(GearItem).filter_by(id=gear_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Gear Item has been deleted")
        return redirect(url_for('sportGear', sport_id=sport_id))
    else:
        return render_template('deletegearitem.html', item=itemToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
