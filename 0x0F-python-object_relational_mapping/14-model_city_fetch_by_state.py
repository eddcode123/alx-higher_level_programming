#!/usr/bin/python3
"""
prints all City objects from the database
"""

from model_city import City
from model_state import State, Base
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
    # delete states containing letter a
    state_city = session.query(City, State)\
        .filter(City.state_id == State.id).order_by(City.id).all()
    for city, state in state_city:
        print(f'{state.name}: {(city.id)} {city.name}')

    # close session
    session.close()
