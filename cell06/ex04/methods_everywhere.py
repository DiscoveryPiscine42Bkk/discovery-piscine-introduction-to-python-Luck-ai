#!/usr/bin/env python3
import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    while len(string) != 8:
        string += "Z"
    print(string)

x = len(sys.argv)
if x <= 2:
    print('none')
else:
    for i in range(1 , len(sys.argv)):
        if len(sys.argv[i]) > 8:
            shrink(sys.argv[i])
        elif  len(sys.argv[i]) < 8:
            enlarge(sys.argv[i])
        else:
            print(sys.argv[i])
            
