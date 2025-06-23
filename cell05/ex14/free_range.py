#!/usr/bin/env python3
import sys

x = len(sys.argv)
if x != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    arr = [i for i in range(start , end + 1)]
    print(arr)
    