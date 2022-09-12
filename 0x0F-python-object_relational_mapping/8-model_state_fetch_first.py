#!/usr/bin/python3
"""
A script that prints the first State object from the database
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
    result = session.query(State).order_by(State.id).first()
    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print('Nothing')


if __name__ == "__main__":
    main()
