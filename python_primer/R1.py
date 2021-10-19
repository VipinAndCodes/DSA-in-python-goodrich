"""
Write a short python function is multile(n,m) that take two 
integer value and returns True if n is a multiple of m, that is,
n = mi for some integer i, and False otherwise

"""

def multiply(n,m):
    
    if m ==0:return False
    return (n%m==0)

print(multiply(5,10))
print(multiply(0,5))
print(multiply(6,0))
print(multiply(10,5))

