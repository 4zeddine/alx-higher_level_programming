#!/usr/bin/python3
"""
script that:
takes in a URL and an email address
sends a POST request to it with an email passed as a parameter
and finally displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.post(url, data={'email': sys.argv[2]})
    print(r.text)
