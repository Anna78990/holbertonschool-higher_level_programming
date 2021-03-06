#!/usr/bin/python3
"""
the class definition of a State and an instance Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

Base = declarative_base()


class State(Base):
    """
    class State, an inherit class of Base
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
