#A constructor is a function that is called automatically when an object is created


#defined a class
class Car:   # we are defining a class by taking a keyword class : class, name_of_class, colon
    speed = 0   # speed is a variable, that is defining property of the class
    started = False # started is also a variable that .... which takes boolean value
    
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
            

# took an object of the class
car1 = Car()
