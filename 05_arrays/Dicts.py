#!/usr/bin/env python3

data={}
count = 5

while len(data) < count:
    var = input("Please insert something: ")
    data[len(data)]=var

print("all dictionary data inserted: ", data)
print(f"these data keys: {data.keys()} \n belong to these data values: {data.values()}")
