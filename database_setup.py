# Configuration code
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# Class definitions with table names and mapper code.
class Sport(Base):
    __tablename__ = 'sport'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    gear_item = relationship('GearItem', cascade='all, delete-orphan')

    @property
    def serialize(self):
        # Return object data in easily serialized format
        return {
            'name': self.name,
            'id': self.id,
        }


class GearItem(Base):
    __tablename__ = 'gear_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    sport_id = Column(Integer, ForeignKey('sport.id'))
    sport = relationship(Sport)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
        }


# End configuration code
engine = create_engine('sqlite:///sportgearwithusers.db')


Base.metadata.create_all(engine)
