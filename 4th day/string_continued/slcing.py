#  create a sting for slicing
#  0 , 1, 2, 3, 4
myString = "Hello World"
print(myString[6])


# reverse a string in python
print(myString[::-1])


# chaining calls

# .replace(), .upper()


# WITH CHAINING
chaining = myString.replace("H", "G").upper()
print(chaining)
# print(myString.replace("H", "G").upper())


# WITHOUT CHAINING
chaining1 = myString.replace("H", "G") #  "Gello World"
chaining2 = chaining1.upper()  # "GELLO WORLD"
print(chaining2)


#  how to print output

a = 4
print(f"the vale of a is : {a}")

b = 10
print(b)

print(" the value of b is :", b)
print(" the value of a  is ", a)

print(f"the value of b is : {b} and the  value of a is {a}")

# print the name and age with f funcion
name = " Gautam"
age = 22

print(f"my name is {name}, and my age is { age}")


#  '', " ", """   """

#  split funciton
yourString = "your name"

# z = yourString.split(' ')
# print(z)

print(yourString.split(' '))

