#!/usr/bin/python3
def roman_to_int(roman_string: "str") -> "int":
    rm_sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_int = 0
    flag = True
    if roman_string and isinstance(roman_string, str):
        rm_str = roman_string.strip()
        for i in range(len(rm_str)):
            if rm_str[i] in rm_sym:
                roman_int += rm_sym.get(rm_str[i])
            else:
                return 0
            if i > 0 and flag:
                if (rm_str[i] == 'V' or rm_str[i] == 'X') \
                        and rm_str[i - 1] == 'I':
                    roman_int -= 2
                    flag = False
                    continue
                elif (rm_str[i] == 'L' or rm_str[i] == 'C') \
                        and rm_str[i - 1] == 'X':
                    roman_int -= 20
                    flag = False
                    continue
                elif (rm_str[i] == 'D' or rm_str[i] == 'M') \
                        and rm_str[i - 1] == 'C':
                    roman_int -= 200
                    flag = False
                    continue
            flag = True
        return roman_int
    return 0
