#!/usr/bin/python3
def add_tuple(tuple_a=(0, 0), tuple_b=(0, 0)):
    if len(tuple_a) >= 2:
        tuple_a = tuple_a[:2]
    if len(tuple_b) >= 2:
        tuple_b = tuple_b[:2]
    if len(tuple_a) == 1:
        tuple_a = tuple_a + (0,)
    if len(tuple_b) == 1:
        tuple_b = tuple_b + (0,)
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return (0, 0)
    if len(tuple_a) == 0:
        return tuple_b
    if len(tuple_b) == 0:
        return tuple_a
    nw_tup = []
    for i in range(2):
        nw_tup.append(tuple_a[i] + tuple_b[i])
    return tuple(nw_tup)
