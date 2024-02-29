# string is a sequence of characters
# adkfn, 23434

num = "adbd"
print(type(num))

#A Python string needs quotes around it
# 'hello world'

# >>> 'a' + 'b'
# 'ab'
# >>> 'ab' * 4
# 'abababab'

# Single or double quotes?
# it's Gautam

# single quotation
name = 'gautam' 
print(name)


#Double quotaion
name2 = "it's kumar"
print(name2)

# tripple quote

saying = """Modi said," India is a developing country" """
print(saying)


# Escaped sequence
# \n, \r, \t, \\

sur = " I am studying in Andhra University \t I am in visakhaptanam from 2 years \r"

print(sur)


# String operations

# a = "i am Studying"

# c = a.capitalize()
# print(c)

# lowercase
mystring = "Hello  world"
c = mystring.lower()
print(c)  # hello world


# upperCase
d = mystring.upper()
print(d)

# length of the string

length = len(mystring)
print(length)

# split function

spl = mystring.split()
print(spl)

# replace 
rep = mystring.replace("H",'r')
print(rep) #rello  world

# Reversing a string (slicing)
rever = reversed(mystring)
print(rever)