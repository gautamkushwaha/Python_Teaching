# format string

name = "Gautam Kumar"
age = 22
print("My name is",name + " and my age is",age )


#with format string we can do just by keeping the format string " f" and the variables inside the midddle bracket
print(f"My name is {name} and my age is {age}")


# with 2 decimals(property of floating point integer)
price = 59
txt = f"The price is {price:.4f} dollars"
print(txt)

# can do the operation inside the format strings

txt = f"The price is {20 * 59} dollars"
print(txt)

