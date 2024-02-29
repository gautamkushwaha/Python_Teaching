#  Python Program to Find All File with .txt Extension Present Inside a Directory
import os, glob

os.chdir("/Users/gautam/Desktop/python_learning/questions")

for file in glob.glob("*.txt"):
    print(file)
