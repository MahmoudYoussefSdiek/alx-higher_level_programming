#!/usr/bin/python3
"""Script to print all City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State


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

    # Retrieve all City objects and display the results
    cities = session.query(State.name, City.id, City.name).join(
        City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    # Close the session
    session.close()
