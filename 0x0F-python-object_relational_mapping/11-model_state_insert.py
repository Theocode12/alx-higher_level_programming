#!/usr/bin/python3
"""
A script that prints the State object
with the name passed as argument
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
    s1 = State(name='Louisiana')
    session.add(s1)
    session.commit()
    print(s1.id)


if __name__ == "__main__":
    main()
