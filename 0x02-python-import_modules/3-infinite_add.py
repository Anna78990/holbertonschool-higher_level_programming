#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    sum = 0
    if argc >= 1:
        for i in range(1, argc):
            a = argv[i]
            a = int(a)
            sum += a
        print("{}".format(sum))
    else:
        print("0")
