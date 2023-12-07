#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list.count(search)
    our_list = [replace if num == search else num for num in my_list]
    return our_list
