from flask import Flask
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
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    return output


# Create route for newGearItem function
@app.route('/sport/<int:sport_id>/new/')
def newGearItem(sport_id):
    return "page to create a new gear item. Task 1 complete!"


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
