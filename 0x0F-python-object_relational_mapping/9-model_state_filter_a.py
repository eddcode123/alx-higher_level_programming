#!/usr/bin/python3
"""
 lists all State objects that contain the letter a in a database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    # create a connection string
    connection_string = (
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/'
        f'{sys.argv[3]}'
        )

    # create an engine
    engine = create_engine(connection_string, pool_pre_ping=True)
    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # query to list all states
    states = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')
    # close session
    session.close()
