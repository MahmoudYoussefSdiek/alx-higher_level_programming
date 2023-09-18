#!/usr/bin/python3
"""
Module to delete all State objects with a name containing the
letter "a" from the database
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

    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects with a name containing the letter "a"
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the State objects from the session
    for state in states:
        session.delete(state)

    # Commit the session to persist the changes to the database
    session.commit()

    # Close the session
    session.close()
