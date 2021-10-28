"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

"""

def sumOfIncreasingTwo():
    a=0
    factor = 0
    while True:
        yield a
        factor += 1
        a += factor*2


gen = sumOfIncreasingTwo()
s = [next(gen) for _ in range(10)]
print(s)


#####################################################
def listcompr():
    return [idx*x for idx, x in enumerate(range(1,11))]

print(listcompr())
