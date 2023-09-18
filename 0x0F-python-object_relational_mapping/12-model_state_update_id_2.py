#!/usr/bin/python3
"""Module to change the name of a State object in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Change the name of the State object to "New Mexico"
    if state is not None:
        state.name = "New Mexico"

    # Commit the session to persist the changes to the database
    session.commit()

    # Close the session
    session.close()
