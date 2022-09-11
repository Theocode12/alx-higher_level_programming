#!/usr/bin/python3
"""
 a script that lists all cities from the database
"""
import MySQLdb
from sys import argv


def main():
    """Main function"""
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, db=database)
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM cities JOIN
            states ON cities.state_id = states.id ORDER BY cities.id"""
    cur.execute(query)
    result = cur.fetchall()
    for row in result:
        print(row)


if __name__ == '__main__':
    main()
