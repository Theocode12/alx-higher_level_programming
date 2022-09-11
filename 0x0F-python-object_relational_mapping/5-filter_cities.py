#!/usr/bin/python3
"""
A script that takes in the name of a state as an
argument and lists all cities of that state
"""
import MySQLdb
from sys import argv


def main():
    """Main function"""
    username = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, db=database)
    cur = db.cursor()
    query = """SELECT cities.name FROM states JOIN cities
            ON states.id = cities.state_id
            AND states.name = %s ORDER BY cities.id"""
    cur.execute(query, (name,))
    result = cur.fetchall()
    cites = []
    for row in result:
        cites.append(row[0])
    print(", ".join(cites))


if __name__ == '__main__':
    main()
