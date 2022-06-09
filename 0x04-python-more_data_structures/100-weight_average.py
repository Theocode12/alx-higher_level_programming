#!/usr/bin/python3
def weight_average(my_list: 'list' = []) -> int:
    if my_list:
        numerator = 0
        denom = 0
        for score, weight in my_list:
            numerator += score * weight
            denom += weight
        return numerator / denom
    return 0
