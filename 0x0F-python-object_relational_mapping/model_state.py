#!/usr/bin/python3
""" Define a state class and link to data base """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Class represents States """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement='auto', unique=True, nullable=False)
    name = Column(String(128), nullable=False)
