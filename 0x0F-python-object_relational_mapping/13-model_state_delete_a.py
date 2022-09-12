#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter a
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
    session.query(State).filter(State.name.ilike('%a%')).\
        delete(synchronize_session='fetch')
    session.commit()


if __name__ == "__main__":
    main()
