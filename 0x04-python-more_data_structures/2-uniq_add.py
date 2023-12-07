#!/usr/bin/python3
def uniq_add(in_list=[]):
    sum = 0
    for i in set(in_list):
        sum += i
    return sum
