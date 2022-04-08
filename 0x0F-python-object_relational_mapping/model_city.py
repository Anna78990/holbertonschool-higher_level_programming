#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from model_state import Base, State

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer)
