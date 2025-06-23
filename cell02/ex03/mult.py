#!/usr/bin/env python3
first_no = int(input("Enter the first number:\n"))
second_no = int(input("Enter the second number:\n"))
mult = first_no * second_no
print(f"{first_no} x {second_no} = {mult}")
if mult > 0:
    print("The result is positive\n")
elif mult < 0:
    print("The result is negative\n")
else:
    print("The result is both positive and negative")