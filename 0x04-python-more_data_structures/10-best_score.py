#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_key = ""
        best_value = list(a_dictionary.values())[0]
        for key, value in a_dictionary.items():
            if best_value <= value:
                best_key = key
                best_value = value
        return best_key
    return
