#!/usr/bin/python3
"""
List all states object from a database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Main function to list all states from the database.
    """
    # Create a connection string
    connection_string = f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}'

    # Create an engine
    engine = create_engine(connection_string)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to list all states
    for state in session.query(State).order_by(State.id):
        print(f'{state.id}: {state.name}')


if __name__ == '__main__':
    main()
