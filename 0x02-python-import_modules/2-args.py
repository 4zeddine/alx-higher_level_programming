#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    i = len(argv) - 1

    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:")
    else:
        print("{}: arguments:".format(i))
    for j in range(i):
        print("{}: {}".format(j + 1, argv[j + 1]))
