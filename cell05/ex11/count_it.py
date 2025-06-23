#!/usr/bin/env python3
import sys
x = len(sys.argv)
if x == 1:
    print("none")
else:
    print("Parameters: " + str(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
