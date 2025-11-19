#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    args = sys.argv[1:]

    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} argument:" if argc == 1 else f"{argc} arguments:")

        for i in range(argc):
            print(f"{i + 1}: {args[i]}")
