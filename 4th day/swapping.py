#Python Program to Swap Two Variables

# take input from the user 
x = int(input("give the first value: "))
y = int(input("Give the second value: "))

#  define a temporary varaible and put the value of first variable in the temp variable
temp = x
x = y
y = temp

print(" the value of x after swapping:", x)
print(" the value of Y after swapping",y)