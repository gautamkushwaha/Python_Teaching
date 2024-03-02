#Python Program to Convert Two Lists Into a Dictionary

index = [1,2,3,4]
language = ['python', 'c', 'c++']

# Using Zip and dictionary method

dictionary = dict(zip(index, language))
print(dictionary)


# using list comprehension

dictionary2 = {k: v for k, v in zip(index, language) }

print(dictionary2)