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
            session.query(State)
            .where(State.id == 2)
            .first()
    )
    if states is not None:
        states.name = "New Mexico"
        session.commit()
    else:
        print("Not found")
    session.close()
