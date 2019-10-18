#!/usr/bin/env python3

#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

input()

# > Indentation
# If statement, without indentation (will raise an error):
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

input()

#if elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

input()
# if elif else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

input()

#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

input()

#Nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
