#!/usr/bin/python3
import sys

argv = sys.argv
argc = len(argv)

if (argc > 1):
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
else:
    print("0 arguments.")
