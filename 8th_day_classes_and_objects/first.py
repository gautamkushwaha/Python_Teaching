# classes and objects in python

# car is a class, when we say car it can be any car, with four wheels, and ohter properties
# student, bird, fish, dog, human beings, building is a class

# object is the name specified of the class
# satish, pigeon, sprawn, bull dog, Gautam, andhra universiry office is a student is a object


# What are Python Methods?


# Method
# When a function is part of an object or Python class, we call it a method.


# Object
# An object is a collection of data (variables) and methods that operate on that data. Objects are defined by a Python class.

# gautam 
# def eat():
#     a = 6
#     b= 60
#     print("when gautam is hungry ,he goes to eat")
#     print(f"{a} is Gautam height and {b} is gautam weight")
    
type('a')  


# creating a python class
class Car:   # we are defining a class by taking a keyword class : class, name_of_class, colon
    speed = 0   # speed is a variable, that is defining property of the class
    started = False # started is also a variable that ....
    
    def start(self):   #start function means , we want to acknoweldge start of parking condition of a car: self?
        self.started = True
        print("The car started")
    
    def increase_speed(self, delta):  # whenever we are taking a method/funciton inside a class, we take self as a parameter to take an 
        if self.started: # after if, there is condition, which returns either true or false
            self.speed = self.speed + delta  # accelearation ( a = a + 5)
            print("Vrooooom")
            
        else:
            print(" You need to start the car first")
        
    def stop(self):
        self.speed = 0
        print("halting")
            

# defining the object and calling the function of the class            
maruti = Car()   # this is the method to define an object
maruti.increase_speed(10)  # calling a mehtod on a python object
maruti.start()
maruti.increase_speed(5)
maruti.stop()



# taking multiple objects of a class
lambergini = Car()
lambergini.start()

honda = Car()
honda.stop()


car4 = Car()

        
        
#This is what’s happening:

# When we call a method on a Python object, Python automatically fills in the first variable, which we call self by convention.
# This first variable is a reference to the object itself, hence its name.
# We can use this variable to reference other instance variables and functions of this object, like self.speed and self.start().

print(id(maruti))
print(id(lambergini))
print(id(honda))
print(id(car4))


maruti.increase_speed(10)
maruti.speed
print(maruti.speed)