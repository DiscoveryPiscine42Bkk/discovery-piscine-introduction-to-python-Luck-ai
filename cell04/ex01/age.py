#!/usr/bin/env python3
age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old")
for i in range(10 , 40, 10):
    print(f"In {i} years, you'll be {i + age} years old.")
