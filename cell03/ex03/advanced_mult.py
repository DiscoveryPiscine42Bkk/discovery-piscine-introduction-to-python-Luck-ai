#!/usr/bin/env python3
import sys
x = len(sys.argv)
if x > 1:
    print("none")
else:
    for i in range(11):
        print(f"\nTable de {i}:", end = '')
        for j in range(11):
            print(f" {i * j}", end='')
