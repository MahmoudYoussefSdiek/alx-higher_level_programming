#!/usr/bin/python3
"""Module to retrieve and display cities from a MySQL database"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
               FROM states
               INNER JOIN cities ON states.id = cities.state_id
               ORDER BY cities.id ASC"""
    # Execute the query to retrieve cities with their corresponding state names
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
