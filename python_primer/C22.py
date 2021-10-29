"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1.

"""
import timeit

from timeit import Timer

def multiply(a,b):
    assert len(a) == len(b)
    c =[None]*len(a)
    for i in range(len(a)):
        c[i] = a[i]*b[i] 
    return c

def mul_Array(a,b):
    c = []
    for a,b in zip(a,b):
        c.append(a*b)
    return c

a, b = [1,2,3,4,5,6], [2,3,4,5,6,7]
print(multiply(a,b))
print(mul_Array(a,b))

print(Timer(lambda: multiply(a,b)).timeit(), Timer(lambda: mul_Array(a,b)).timeit())

