"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""
def sqr(n:int):
    assert type(n) == int ,"Please enter a integer"
    if n>0:
        b = 0
        for i in range(n):
            a = i * i
            b = b + a
            i+=i
        return b
    else:
        return "enter a postive number"

#another method 

def sumsqr(n):
    assert type(n) == int ,"Please enter a integer"
    if n>0:
        return sum(i*i for i in range(1,n))
    else:
        return "enter a postive number"
    

print(sumsqr(5))
print(sumsqr(-5))
# print(sumsqr(-5.02))

print("///////////////////////////////")    
print(sqr(5))
print(sqr(-5))
# print(sqr(-5.02))









    

