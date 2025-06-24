#!/usr/bin/env python3
n = input("Give me a number: ")
try:
    x = float(n)
    if x == int(x):
        print("The number is an integer")
    else:
        print("The number is a decimal")
except ValueError:
        print("Please enter a valid number")
