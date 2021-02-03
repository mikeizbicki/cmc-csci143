#!/usr/bin/python3


# os module built-in to python
# module for interacting directly with system kernel
# most libraries work the same for Windows/Mac/Linux/etc
# os sometimes behaves differently
import os

# list containing all the numbers from 1 - 1 billion
# approximately 8 gigabytes of memory
xs = list(range(1000000000))

# fork actually returns twice, 
# every other function only returns once
# creates a copy of your program in memory, 
# that copy is called the "child process" and it continues
# execution just like the original
n = os.fork()

# in an OS course for CS majors,
# fork() is the key thing that the course is built around

'''
called a fork bomb
while True:
    os.fork()
'''

if n==0:
    print("we're the child")
if n>0:
    print("we're the parent")

while True:
    continue

print('hello')
