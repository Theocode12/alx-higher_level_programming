#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nw_list = []
    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                nw_list.append(result)
            except (ValueError, TypeError):
                print("wrong type")
                nw_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                nw_list.append(0)
            except IndexError:
                print("out of range")
                nw_list.append(0)
    finally:
        return nw_list
