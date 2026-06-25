#!/usr/bin/python3
""" List state from database """


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = (
            session.query(State).
            filter(State.name.like('%a%'))
            .all()
    )
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
