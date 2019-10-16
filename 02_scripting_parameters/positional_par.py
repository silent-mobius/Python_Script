#!/usr/bin/env python3
import sys


print('the name of script is ', sys.argv[0])  #printing script name

print(f'if you have provided positional param, it is {sys.argv[1]}') # getting first param

print(f'if you have provided another positional param, it is {sys.argv[2]}') # getting 2 param

print(f'if you have provided several params, these would be {sys.argv[1:]}') # getting first param
