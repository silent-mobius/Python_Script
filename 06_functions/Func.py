#!/usr/bin/env python3


#declaring the function
def my_function():
  print("Hello from a function") 

#calling function
my_function() 

# another declaration with argument
def my_other_function(fname):
    print(fname + " Meyer")


my_other_function('Mark')
my_other_function('Michael')
my_other_function('Alex')

# yes, yet another useless function that gets several parameters
def my_useless_function(fname, lname):
    print(fname + "\n" + lname)


my_useless_function("Alex", "Schapelle")

# yes, same  useless function that gets several pre-set parameters
def my_useless_function2(fname="Alex", lname="Schapelle"):
    print(fname + "\n" + lname)

my_useless_function2('Arnold','Knoles') # if you don't get the joke seek for beyonces meme on 9gag


# in case there is infinite arguments and you wish it to work like List(AKA Arbitrary Arguments, *args)
def my_counting_function( *stuff):
    for s in stuff:
        print(s)

my_counting_function('stuff_1','stuff_2','stuff_3','stuff_4')

# in case there is infinite arguments and you wish it to work like Dict(AKA Arbitrary Keyword Arguments, **kwargs)
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print(f"{key}=={value}")

greet_me(name="Yoda") # watch star war for Gods sake...

## returning the value
def count_func(x):
      return 2 * x

print(count_func(2))
print(count_func(4))
print(count_func(8))