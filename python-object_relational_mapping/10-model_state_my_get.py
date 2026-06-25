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
            where(State.name == sys.argv[4])
            .first()
    )
    if states is not None:
        print(states.id)
    else:
        print("Nothing")
    session.close()
