"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""
from timeit import Timer

def reversedcopyarray(array):
    reversed_array = [None]*len(array)
    for i in range(len(array)):
        reversed_array[len(array)-1-i] = array[i]
    return reversed_array

data = [1,2,5,8,9,7,5]
print(reversedcopyarray(data))


# ////////////////////////////////////////////////////////////

def reversearray(arr):
    i=0
    l=len(arr)
    while i < l//2:
        arr[i],arr[l-i-1] = arr[l-i-1],arr[i]
        i+=1
        return arr

print(reversearray(data))



print(Timer(lambda: reversedcopyarray(data)).timeit(), Timer(lambda: reversearray(data)).timeit())
