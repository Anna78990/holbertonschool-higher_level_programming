#!/usr/bin/python3
for i in range(0, 10):
    for n in range(0, 10):
        if i < n:
            if i >= 0 and n > 1:
                print(', ', end="")
            print('{:d}{:d}'.format(i, n), end="")
        else:
            continue
print('')
