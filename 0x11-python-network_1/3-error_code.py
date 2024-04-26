#!/usr/bin/python3
"""A script that:
that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8)
manages urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print('Error code:', e.code)
