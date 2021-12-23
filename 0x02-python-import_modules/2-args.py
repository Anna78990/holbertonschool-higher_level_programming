#!/usr/bin/python3
import sys

argvs = sys.argv
argc = len(argvs)

if (argc > 1):
    for i in range(1, argc):
        print("{}: {}".format(i, argvs[i]))
else:
    print("0 arguments.")
