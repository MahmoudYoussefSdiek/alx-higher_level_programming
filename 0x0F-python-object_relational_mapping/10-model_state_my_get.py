#!/usr/bin/python3
"""
Module to print the State object with the specified name from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the State object with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close the session
    session.close()
