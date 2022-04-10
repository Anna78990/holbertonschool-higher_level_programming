#!/usr/bin/python3
"""
displays all values where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    arg = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                           passwd=arg[2], db=arg[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name = '%s' ORDER BY id ASC" % arg[4])
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
