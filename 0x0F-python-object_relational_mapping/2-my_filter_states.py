#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa
where the name matches the provided argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create cursor object
    cursor = db.cursor()

    # Execute the query to select states matching the provided name
    query = """SELECT *
                 FROM states
                 WHERE name LIKE '{:s}' ORDER BY id ASC""".format(state_name)
    cursor.execute(query)

    # Fetch all the rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
