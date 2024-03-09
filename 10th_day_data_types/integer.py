# Basic Data types in python:
# Integers
# Floating point numbers
# Complex numbers
# Booleans
# Strings


# Advance data types in python:
# Tuples
# Lists
# Ranges
# Dictionaries
# Sets

# for i in range(0,100):
#     print(i)
    
#Mutability in Python
# mutable and immutable

#An object is mutable if we can change the data it holds, and it’s immutable if we can’t change it.

# Python data types that are mutable are:

# Lists
# Dictionaries
# Sets


mystring = "Hello"
mycopy = mystring
print(mycopy)   # hello
print(mystring)  # hello

mystring = "world"  # we took the already defined variable and gave another string

print(mystring)
print(mycopy)

# because of this string is a immutable data type

# checking the python data types
print(type(mycopy))
print(type(2))
print(type(2.0))
print(type(False))
print(type(1 + 3j))



#Max size of a Python integer

# the integere value in python is unbound, i. e  there is no limit for the largest value in python


a = 3874384783748384583478473947839789493789478937388494598
a = a + 1
print(a)


# conversion of python data types
mystring = "100"
print(type(mystring))
x = int(mystring)
print(type(x))
 
# form number to string
a  = 200
print(type(a))
mystring = str(a)
print(type(mystring))


# floating number to integer and integer to floating number
a = 2.3
x = int(a)
print(type(a))
print(type(x))


# convrerting integer to floating point

d = 200
k = float(d)
print(type(d))
print(type(k))


#Python random integer

import random
a = random.randint(1, 100)
print(a)