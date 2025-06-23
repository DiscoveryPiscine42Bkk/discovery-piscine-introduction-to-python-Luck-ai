#!/usr/bin/env python3
def greetings(name = 'noble stranger'):
    if isinstance(name , str) == False:
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}")

greetings("Alex")
greetings()
greetings(42)

