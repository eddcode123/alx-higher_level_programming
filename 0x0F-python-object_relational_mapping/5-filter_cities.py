#!/usr/bin/python3
""" list all cities of the state passed """
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
    query = 'SELECT cities.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s ORDER BY cities.id ASC'

    # Execute query
    try:
        cur.execute(query, (sys.argv[4],))
        cities = cur.fetchall()
        print(cities)
        print(", ".join([city[0] for city in cities]))

    except MySQLdb.Error as e:
        print("Error executing query:", e)
        sys.exit(1)

    # Close the cursor
    cur.close()

    # Close the connection
    db.close()
