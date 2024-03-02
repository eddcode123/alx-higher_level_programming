#!/usr/bin/python3
""" displays all values in the states where name == argv[4] """
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

    # Execute query
    try:
        cur.execute('SELECT * FROM states WHERE name = "{}" \
        ORDER BY id ASC'.format(sys.argv[4]))
        results = cur.fetchall()
        # Print results
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print('Query execution error:', e)
        sys.exit(1)

    # Close cursor
    cur.close()
    # Close connection to the database
    db.close()
