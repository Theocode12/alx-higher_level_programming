#!/usr/bin/python3
def multiply_list_map(my_list: 'list' = [], number: 'int' = 0) -> 'list':
    return list(map(lambda x: x * number, my_list))
