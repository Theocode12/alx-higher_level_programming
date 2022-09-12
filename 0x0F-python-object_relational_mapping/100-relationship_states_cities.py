#!/usr/bin/python3
"""
A script that prints the State object
with the name passed as argument
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City


def main():
    """Main function"""
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    s1 = State(name='California')
    c1 = City(name='San Francisco')
    s1.cities.append(c1)
    session.add_all([s1, c1])
    session.commit()


if __name__ == "__main__":
    main()
