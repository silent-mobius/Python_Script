#!/usr/bin/env python3

x = 0

while x<10:
    print(x)
    x +=1

while x>0:
    print(x)
    x -=1

x = input("Please provide your fullname: ")
y=0

while y < len(x):
    print(y)
    y += 1
    

while True:
    num = int(input("please provide number: "))
    x= 0
    while x <= num:
        x += 1
        if (x / 2) and (x % 2):
            print(x)
            break