#!/usr/bin/python3
"""
A script that prints the State object
with the name passed as argumen
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
    name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db), pool_pre_ping=True)
    session = Session(engine)
    result = session.query(State).filter(State.name == name).\
        order_by(State.id).all()
    if result:
        print("{}".format(result[0].id))
    else:
        print("Not found")


if __name__ == "__main__":
    main()
