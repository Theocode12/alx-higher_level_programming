#!/usr/bin/python3
"""
A module that contains the class definition
of a State and an instance declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """My state class"""

    __tablename__ = 'states'

    id = Column(Integer(), nullable=False,  primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade="all, delete")
