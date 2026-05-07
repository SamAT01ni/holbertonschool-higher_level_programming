#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = len(argv)
    if args <= 1:
        print("0 arguments.")
    else:
        if args == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(args - 1))
        for i in range(1, args):
            print("{}: {}".format(i, argv[i]))
