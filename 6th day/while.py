# while <expression evaluates to True>:
#    do something

#is equal to 
a = 5
while (a != 3):  # either a is equal to 4, a = 5: is 5 equal to 4, it means it will return false
    print(" The value of a is 5") # the condition is True, then only it will priint the statement inside the while loop
    break

print(" Priint the outside things") #Priint the outside things
    

# is greater than
#  a>3 , a< 9 , a == 5


# we can print numbers from 1 to 100

# for i in range(1,100):
#     print(i)
    

# print the number from 1 to 100 using while loop

i = 1
while(i <10): # i is less than 100, it will return True all the time, when i is equal to 100: the condition will be false
    print(i)
    i = i+1 # i =2, i=3, i= 4 ......at the last iteration , i =99, 

print("we are out of the loop")


#Infinite loops

while True:  # the condition after while is true, this will return true in each iteration, so the statement inside will be printed infinite time,unless we stop
    print("i live in Tirupati")
    break