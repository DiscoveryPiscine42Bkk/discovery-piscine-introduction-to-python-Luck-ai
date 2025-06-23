#!/usr/bin/env python3
import sys
x = len(sys.argv)
if x != 2:
    print("none")
else:
    string = input("What was the parameter? ")
    if string == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
