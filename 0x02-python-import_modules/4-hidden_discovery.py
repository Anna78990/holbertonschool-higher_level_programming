#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    for attr in dir(hidden_4):
        if attr.startswith('__'):
            continue
        print(attr)
