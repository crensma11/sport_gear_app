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
@app.route('/hello')
def HelloWorld():
    sport = session.query(Sport).first()
    items = session.query(GearItem).filter_by(sport_id=sport.id)
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
    return output


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
