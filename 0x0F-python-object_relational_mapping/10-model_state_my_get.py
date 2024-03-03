#!/usr/bin/python3
"""
 prints the State object with the name passed as argument
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
    # query to id of named state
    state = session.query(State)\
        .filter(State.name == sys.argv[4]).order_by(State.id)\
        .first()
    if state:
        print(f'{state.id}')
    else:
        print('Not found')
