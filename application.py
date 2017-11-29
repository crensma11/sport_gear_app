from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Sport, GearItem
app = Flask(__name__)


engine = create_engine('sqlite:///sportgear.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/sport/<int:sport_id>/')
def sportGear(sport_id):
    sport = session.query(Sport).filter_by(id=sport_id).one()
    items = session.query(GearItem).filter_by(sport_id=sport.id)
    return render_template('gear.html', sport=sport, items=items)


# Create route for newGearItem function
@app.route('/sport/<int:sport_id>/new/', methods=['GET', 'POST'])
def newGearItem(sport_id):
    if request.method == 'POST':
        newItem = GearItem(name=request.form['name'], sport_id=sport_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('sportGear', sport_id=sport_id))
    else:
        return render_template('newgearitem.html', sport_id=sport_id)


# Create route for editGearItem function
@app.route('/sport/<int:sport_id>/<int:gear_id>/edit/')
def editGearItem(sport_id, gear_id):
    return "page to edit a gear item. Task 2 complete!"


# Create route for deleteGearItem function
@app.route('/sport/<int:sport_id>/<int:gear_id>/delete/')
def deleteGearItem(sport_id, gear_id):
    return "page to delete a gear item. Task 3 complete!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
