#!/usr/bin/python3
def remove_char_at(str, n):
    s = str
    s = s[:n] + s[n+1:]
    return s
