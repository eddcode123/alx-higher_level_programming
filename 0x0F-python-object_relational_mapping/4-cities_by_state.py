#!/usr/bin/python3
""" list all cities """
import MySQLdb
import sys

if __name__ == '__main__':
    # Create a connection to the database
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    # Get cursor
    cur = db.cursor()

    # Create a query
    query = 'SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id ASC'

    # Execute query
    try:
        cur.execute(query)
        result = cur.fetchall()
        # Print results
        for row in result:
            print(row)
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        sys.exit(1)

    # Close the cursor
    cur.close()

    # Close the connection
    db.close()
