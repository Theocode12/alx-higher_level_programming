#!/usr/bin/python3
"""
A script that lists all State objects,
and corresponding City objects
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State
from relationship_city import City


def main():
    """Main function"""
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db), pool_pre_ping=True)

    session = Session(engine)
    states = session.query(State).outerjoin(City).order_by(State.id, City.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    main()
