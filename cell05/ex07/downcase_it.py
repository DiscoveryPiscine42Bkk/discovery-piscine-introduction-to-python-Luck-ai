#!/usr/bin/env python3
import sys
x = len(sys.argv)
if x != 2:
    print("none")
else:
    print(sys.argv[1].lower())

