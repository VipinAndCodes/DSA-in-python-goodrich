"""
Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function

"""


def sumSqrOdd(n):
    assert type(n) == int ,"Please enter a integer"
    return (sum(i*i for i in range(1,n) if i%2 ==1)) if n>0 else False


print(sumSqrOdd(5))
print(sumSqrOdd(-5))
