#!/usr/bin/python3
"""
prints the State object with the name passed as argument
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    dic = {}
    for state in session.query(State).order_by(State.id).all():
        dic[state.name] = state.id
    if sys.argv[4] in dic.keys():
        ar = sys.argv[4]
        print(dic[ar])
    else:
        print("Not found")
    session.close()
