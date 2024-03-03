#!/usr/bin/python3
"""
list all states object from a database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    # create a connection string
    connection_string = f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}'
    # create an engine
    engine = create_engine(connection_string)
    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # query to list all states
    for state in session.query(State).order_by(State.id):
        print(f'{state.id}: {state.name}')
