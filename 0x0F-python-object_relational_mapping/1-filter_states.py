#!/usr/bin/python3
""" lists all states with a name starting with N from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == '__main__':
    # create a connection to database
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
    except MySQLdb.Error as e:
        print("Error connecting to Mysql: ", e)
        sys.exit(1)

    # Get cursor
    cur = db.cursor()

    # execute query
    try:
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        results = cur.fetchall()
        # print result
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print('Query execution error: ', e)
        sys.exit(1)

    # close cursor
    cur.close()
    # close connection to database
    db.close()
