print()

print(1234)
print( " I like Visakhaptanam")
print("visakhapatnam is the 10th largest economically rich city", 1000000)
print(True)
a = 5
print(a)

# there are two kinds of functions
# 1. user definded function
# 2. library function
# 2. library functions means already defined functions like print(), input(), randint(), squrt(), len(), upper()

# 1. user define function


# defining the functions
def multiply():
    a = 5
    b = 10
    print(a *b)


# function call
multiply()


# user to give the number, argument wala function, function with arguments

def multiply(a,b):
    print(a*b)
  

a = int(input("Enter the first value: "))    
b = int(input("Give the second value: "))
multiply(a,b)


#  making a simple calcualtor using function

def sum(a, b):
    print(a+b) 

def substaction(a,b):
    print(a-b)
    
def multiply(a, b):
    print(a * b) 
    
def divide(a,b):
    print(a /b)
    
a = int(input("Enter the value of a: "))
b = int(input(" enter the value of b: ")) 
 
sum(a,b)
substaction(a,b)
multiply(a,b)
divide(a,b)  

print()