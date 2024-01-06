#!/usr/bin/python3
def no_c(my_string):
    letters = 'cC'
    removed = [
            char for char in my_string
            if char not in letters
    ]
    new = ''.join(removed)
    return new
