#!/usr/bin/python3
"""
a script that lists all states with a name starting with N (upper N)
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
    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id""")
    result = cur.fetchall()
    for row in result:
        print(row)


if __name__ == '__main__':
    main()
