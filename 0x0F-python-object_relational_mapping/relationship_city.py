#!/usr/bin/python3
"""
A module that contains the class definition
of Cites and an instance declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """My city class"""

    __tablename__ = "cities"
    id = Column(Integer(), nullable=False,  primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
