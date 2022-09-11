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

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    result = cur.fetchall()
    for row in result:
        print(row)


if __name__ == '__main__':
    main()
