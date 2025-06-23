#!/usr/bin/env python3
def downcase_it(array):
    for i in range(1 , len(array)):
        print(array[i].lower())

import sys

s = len(sys.argv)
if s == 1:
    print('none')
else:
    downcase_it(sys.argv)

 