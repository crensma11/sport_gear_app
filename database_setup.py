# Configuration code
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Class definitions with table names and mapper code.
class Sport(Base):
    __tablename__ = 'sport'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class GearItem(Base):
    __tablename__ = 'gear_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    sport_id = Column(Integer, ForeignKey('sport.id'))
    sport = relationship(Sport)


# End configuration code
engine = create_engine('sqlite:///sportgear.db')


Base.metadata.create_all(engine)
