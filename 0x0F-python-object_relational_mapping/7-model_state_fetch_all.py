#!/usr/bin/python3
"""
A script that lists all State objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def main():
    """Main function"""
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db), pool_pre_ping=True)
    session = Session(engine)
    result = session.query(State).order_by(State.id).all()
    for state in result:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    main()
