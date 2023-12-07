#!/usr/bin/python3
def roman_to_int(romanstring):
    total = 0
    prv_num = 0
    if not isinstance(romanstring, str) or romanstring is None:
        return 0
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for num in reversed(romanstring):
        val = nums.get(num, 0)

        if val < prv_num:
            total -= val
        else:
            total += val

        prv_num = val
    return total
