# from the text



# there are mainly two scopes of variable
# 1. Global variable
answer = "good morning"
def say_hi():
    print("Hi", name)
    print(answer)
    
name = 'Erik'
say_hi()

print(answer)


#  local variable
b = 8   # global variable
def variable_scope():
    a = 10     # local variable
    print(a + b)
    
variable_scope()

print(b +a)


# global variable can be reached inside the function and anywhere in the program 
# but local variable can't be reached or used from outside the function or outside of the context in which it is defined
