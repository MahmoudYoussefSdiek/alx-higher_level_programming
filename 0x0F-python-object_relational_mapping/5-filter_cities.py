#!/usr/bin/python3
"""
Script to retrieve and display cities of a state from a MySQL database
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Create the SQL query using parameterized query
    query = """SELECT cities.name FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s ORDER BY cities.id ASC"""

    # Execute the query to retrieve cities of the specified state
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    cities = [row[0] for row in results]
    print(", ".join(cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()
