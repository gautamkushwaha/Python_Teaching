#Python Program to Get the Class Name of an Instance
class vehicle:
    def name(self,name):
        return name
    
v = vehicle()

print(v.__class__.__name__)
print(type(v).__name__)