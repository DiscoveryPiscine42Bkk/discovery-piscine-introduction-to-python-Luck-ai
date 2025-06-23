#!/usr/bin/env python3
import sys
import re
x = len(sys.argv)
if x != 3:
    print("none")
else:
    search = re.findall(sys.argv[1] , sys.argv[2])
    print(len(search))