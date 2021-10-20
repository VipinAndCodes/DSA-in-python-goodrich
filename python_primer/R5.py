"""
Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.
"""

def sumsqr(n:int):
    return sum(i*i for i in range(1,n)) if n > 0 else False
    


print(sumsqr(5))
print(sumsqr(-5))
print(sumsqr(-5.02))