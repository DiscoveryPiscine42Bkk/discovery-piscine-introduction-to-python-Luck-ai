#!/usr/bin/env python3
def array_of_names(names):
    array = [start.capitalize() + " " + end.capitalize() for start , end in names.items()]
    return array

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"    
}

print(array_of_names(persons))