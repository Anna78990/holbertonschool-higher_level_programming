#!/usr/bin/python3
"""
lists all of elements
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City

if __name__ == "__main__":
    a = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(a[1], a[2], a[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    for state, city in session.query(State, City)\
            .filter(City.State_id == state.id)\
            .order_by(City.id):
        print("{} :({}) {}".format(state.name,
                                   city.id, city.name))
    session.close()
