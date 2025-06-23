#!/usr/bin/env python3
count = 0 
import sys
x = len(sys.argv)
if x != 2:
    print("none")
else:
    for i in sys.argv[1]:
        if i == 'z':
            print('z', end = '')
            count+= 1
    if count == 0:
        print("none")
    else:
        print()



    