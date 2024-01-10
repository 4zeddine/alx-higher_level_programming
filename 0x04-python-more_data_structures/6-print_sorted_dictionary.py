#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = list(a_dictionary.keys())
    sorted_list.sort()
    for item in list_ord:
        print("{}: {}".format(item, a_dictionary[item]))
