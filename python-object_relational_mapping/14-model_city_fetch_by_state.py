#!/usr/bin/python3
""" List state from database """


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db))

    Session = sessionmaker(bind=engine)
    session = Session()
    statecity = (
            session.query(State, City).
            filter(State.id == City.state_id)
            .order_by(City.id)
            .all()
    )
    for state, city in statecity:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
