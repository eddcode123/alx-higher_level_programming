#!/usr/bin/python3
"""
changes the name of a State object from the database.
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
    # update name
    update_name = session.query(State).filter_by(id=2).first()
    update_name.name = 'New Mexico'
    # commit transaction
    session.commit()

    # close session
    session.close()
