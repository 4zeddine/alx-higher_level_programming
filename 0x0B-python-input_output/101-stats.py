#!/usr/bin/python3
"""reads stdin line by line and computes metrics."""
import sys

if __name__ == "__main__":
    size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """prints the accumulated stats."""
        print("File size: {}".format(size[0]))
        for key in sorted(codes.keys()):
            if codes[key]:
                print("{}: {}".format(key, codes[key]))

    def check_match(line):
        """checks for a regexp match in line."""
        try:
            line = line[:-1]
            words = line.split(" ")
            size[0] += int(words[-1])
            code = int(words[-2])
            if code in codes:
                codes[code] += 1
        except:
            pass

    i = 1
    try:
        for line in sys.stdin:
            check_match(line)
            if i % 10 == 0:
                print_stats()
            i += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
