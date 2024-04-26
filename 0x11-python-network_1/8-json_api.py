#!/usr/bin/python3
"""
script that
takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
    Display Not a valid JSON if the JSON is invalid
    Display No result if the JSON is empty
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
