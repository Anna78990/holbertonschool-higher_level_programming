#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        listOfValues = a_dictionary.values()
        listOfValues = list(listOfValues)
        mx = max(listOfValues)
        for k, v in a_dictionary.items():
            if v == mx:
                cle = k
                return cle
        return None
