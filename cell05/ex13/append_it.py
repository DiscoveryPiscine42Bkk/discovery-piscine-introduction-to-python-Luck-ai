#!/usr/bin/env python3
import sys
import re

x = len(sys.argv)
if x == 2:
    print('none')
else:
    for i in range(1 , len(sys.argv)):
        if len(re.findall("ism" , sys.argv[i])) > 0:
            pass
        else:
            print(sys.argv[i] + "ism")
