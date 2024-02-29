#A Python function is a named section of a program that performs a specific task and, optionally, returns a value

def add(a, b,c):
    return(a+b )




c = add(9,8,8)
print( " the value of c is :",c, " from the addition of two numbers a, and b that we passed as an argument")


d = add(10,14,24)
print(d)

e = add(10,34,45)
print(e)

#  code reusibility
# modules and packages.

# Built-in Python functions
print('Hello, readers!')

print(15)

result = print('Hello')
print(result)

print(print('Hello'))

#None is a special type of value in Python, basically meaning ‘nothing.’


# len() is a library function that return the length of the string
mylength = len('Hello ')  #6
print(mylength)


my_string = "hello world" # my_string is a variable that stores the string " Hello world"
length_my_string = len(my_string) #length_my_string is another variable that stores the length of my_stirng which is 11
print(length_my_string) # this prints whatever is the value of length_my_string, 11



#creating a python function

def hii(): # defination of the function , def <name of the function>():, and inside this function we give the statements
    print("Hii")
    
    
hii()  # we are calling the functions



# python functions parameters and arguments

def greeting(name):
    print("Good Morning\t", name)

greeting("Ram")

greeting("sita")

greeting("Jagan Mohan REddy")


#Python function with multiple arguments


def intro(name, location, work):
    print(" my name is", name, " and i live in", location," I do ",work,"for my living ")
    print(f"my name is {name}. I live in {location} and I do {work} for my living") # f function prints the things inside the quotation mark only , we have to take that variable or argument inside the middle bracket
    
intro("Gautam","visakhapatnam","full stack development" )

intro("Sai Satish", "Tirupati","run a business")

intro("narendra Modi", "Delhi", " politics")


# returning values

def add(a,b):
    return a+b

c = add(5,7)
print(c)


# sub(a,b): return a-b, mul(a, b): return a*b, we can do multiply, to the power of with **, % ,//,




# if else statemnet

a = 4
if a == 5:
    print("a is equal to 5")
    
else:
    print(" a si not equals to 5")
    
  
# voting right

# take input from the user
age = int(input("Enter your age"))

if age > 18:
    print(" you are eligible to vote ")
else:
    print("you are not eligible to vote")  
    
if add(5,5) == 12:  # add(5,5 ) will return 10. so there will be comparison because comparison operator, 10 will be compared with 10
    print("tha is what we expected")
    
    
    
# empty return statement

def tirupati():
    print("i went to tirupati but didn't brought anything")
    return 
 
c= tirupati()
print(c)


#
 