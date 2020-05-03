#!/usr/bin/env python3

data=()
count = 5

while len(data) < count:
    var = int(input("Please insert number: "))
    data=var, # will stuck in infinite loop --> can not resize the tuple

print("all Tuple data inserted: ", data)
