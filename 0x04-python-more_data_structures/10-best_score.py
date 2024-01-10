#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        max_score = 0
        leader = ""
        for item in my_list:
            if a_dictionary[item] > max_score:
                max_score = a_dictionary[item]
                leader = item
        return leader
