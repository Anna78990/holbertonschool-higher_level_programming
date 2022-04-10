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
    session = Session(engine)
    for join in session.query(State, City)\
            .join(City, State.id == City.state_id)\
            .order_by(City.id).all():
        print("{} :({}) {}".format(join.State.name,
                                   join.City.id, join.City.name))
    session.close()
