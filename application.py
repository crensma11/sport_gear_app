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

# Create route for editGearItem function

# Create route for deleteGearItem function

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
