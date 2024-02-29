# we will apply whatever concept we have learn

# function, if-else , loop, data type, conditional, Boolean

def say_hi(name): # defining the function with a parameter
    if name == '':
        print("You didn't enter your name!")
    else:
        print("Hi there...")
    
    for letter in name:
        print(letter)


name = input("Enter your name :")
say_hi(name) # calling the function , giving the value of parameter

say_hi("")
