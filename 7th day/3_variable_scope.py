# in programming language, variable is having scope


b = 8
def variable_scope():
    a = 10
    print(a + b)
    
variable_scope()

print(b +a)


# from the text
def say_hi():
    print("Hi", name)
    answer = "Hi"
    
name = 'Erik'
say_hi()

print(answer)