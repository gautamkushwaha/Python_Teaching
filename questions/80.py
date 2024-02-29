# python program to get file Name from the file path

import os

#  file name with extension
file_name = os.path.basename('questions/file.txt')


# file name without extension

print(os.path.splitext(file_name)[0])
print(os.path.splitext(file_name))