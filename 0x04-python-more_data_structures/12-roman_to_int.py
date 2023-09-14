#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    ans = 0
    i = 0
    j = i + 1
    ln = len(roman_string)

    while i < ln:

        if j < ln and roman_dict[roman_string[i]] < roman_dict[roman_string[j]]:
            ans = ans + roman_dict[roman_string[j]] - roman_dict[roman_string[i]]
            i += 2
        else:
            ans += roman_dict[roman_string[i]]
            i += 1
    return ans
