#!/usr/bin/python3
"""
 add the State object “Louisiana” to the database
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
    # add new state to table
    add_state = State(name="Louisiana")
    session.add(add_state)
    # commit transaction
    session.commit()
    # print of add state
    print_id = session.query(State).filter(State.name == "Louisiana").first()
    print(f'{print_id.id}')

    # close session
    session.close()
