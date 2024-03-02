#!/usr/bin/python3
import MySQLdb
import sys
""" script that lists all states from the database hbtn_0e_0_usa """


# create a list of arguments
arguments = sys.argv[1:]

# create a conection to the database
db = MySQLdb.connect(host='localhost', user=arguments[1], passwd=arguments[2], db=arguments[3], port=3306)
# get cursor
cur = db.cursor()

# create a query
query = 'SELECT * FROM states ORDER BY id ASC'
# execute query
cur.exectute(query)
result = cur.fetchall()
# print results
for row in result:
    print(row)

# close the cursor
cur.close()
# close the connection
db.close()
