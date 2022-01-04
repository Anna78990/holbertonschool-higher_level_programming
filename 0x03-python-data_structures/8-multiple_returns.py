#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
         s = list(sentence)
         le = len(s)
         return (le, s[0])
    else:
        return (0, None)
