#!/usr/bin/env python3
n = input("Give me a number: ")
try:
    if int(n):
        print("The number is an integer")
except:
    if float(n):
        print("The number is a decimal")