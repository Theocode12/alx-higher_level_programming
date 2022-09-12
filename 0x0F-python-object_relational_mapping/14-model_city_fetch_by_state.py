#!/usr/bin/python3
"""
A script that prints all City objects from the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


def main():
    """Main function"""
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db), pool_pre_ping=True)
    session = Session(engine)
    result = session.query(State.name, City.id, City.name).\
        join(State).order_by(City.id)
    for city in result:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))


if __name__ == "__main__":
    main()
