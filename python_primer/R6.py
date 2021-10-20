"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.

"""

def sumSqrOdd(n):
    assert type(n) == int ,"Please enter a integer"
    return (sum(i*i for i in range(1,n) if i%2 ==1)) if n>0 else False


print(sumSqrOdd(5))
print(sumSqrOdd(-5))
