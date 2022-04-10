#!/usr/bin/python3
"""
SQL Injection for 2-my_filter_states.py
"""

import sys
import MySQLdb

if __name__ == '__main__':
    arg = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                           passwd=arg[2], db=arg[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name = %(name)s ORDER BY id ASC", {'name': arg[4]})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
