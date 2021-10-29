"""
Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.

"""

# Brute force solution (bad)

import random

def custom_shuffle(data):
    array = [None]*len(data)
    used_indices = set()
    for i in range(len(data)):
        added = False
        while added == False:
            choice = random.randint(0,len(data)-1)
            if choice not in used_indices:
                array[choice] = data[i]
                used_indices.add(choice)
                added = True


    return (array)

x = [1,2,3,4,5,6,7,8,9,10]
print(custom_shuffle(x))
random.shuffle(x)
print(x)

#Gradual swap solution

def Gradual_swap(data):
    l = len(data)
    for i in range(l):
        choice = random.randint(0,(l-1-i))
        data[choice],data[l-1-1]=data[l-1-1],data[choice]


print('\nInplace shuffle method')
data = [1,2,3,4,5,6]
Gradual_swap(data)
print(data)

