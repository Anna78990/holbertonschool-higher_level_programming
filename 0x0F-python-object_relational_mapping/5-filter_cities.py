#!/usr/bin/python3
"""
takes an argument and lists all cities of the state
"""
import sys
import MySQLdb

if __name__ == '__main__':
    arg = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                           passwd=arg[2], db=arg[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %(states.name)s \
                 ORDER BY cities.id ASC", {'states.name': arg[4]})
    query_rows = cur.fetchall()
    i = 0
    for row in query_rows:
        str = ''.join(row)
        if i == 0:
            print('{}'.format(str), end="")
        else:
            print(', {}'.format(str), end="")
        i += 1
    print()
    cur.close()
    conn.close()
