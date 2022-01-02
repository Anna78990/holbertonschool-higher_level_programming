#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 2) != 0:
        m = i - 32
        print('{}'.format(chr(m)), end="")
    else:
        print('{}'.format(chr(i)), end="")
