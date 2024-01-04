#!/usr/bin/python3
import sys
argv = sys.argv
i = len(argv)
j = 1

if len(argv) == 1:
    print("0 arguments.")
elif len(argv) == 2:
    print("1 argument:")
    print("1: {}".format(argv[1]))
else:
    print("{}: arguments:".format(i - 1))
    while j < i:
        print("{}: {}".format(j, argv[j]))
        j += 1
