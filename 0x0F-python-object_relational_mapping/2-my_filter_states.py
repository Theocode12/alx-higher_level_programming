#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
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
    query = """SELECT * FROM states WHERE name = '{:s}'
            ORDER BY states.id""".format(name)
    cur.execute(query)
    result = cur.fetchall()
    for row in result:
        if row[1] == name:
            print(row)


if __name__ == '__main__':
    main()
