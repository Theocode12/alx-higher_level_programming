#!/usr/bin/python3
"""
A script that changes the name of a State object
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
    state = session.query(State).get(2)
    state.name = 'New Mexico'
    session.add(state)
    session.commit()


if __name__ == "__main__":
    main()
