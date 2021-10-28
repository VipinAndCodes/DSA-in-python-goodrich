"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.

"""
data=[1,2,3,4,5]


def product(a):
    for i in a:
        for j in a:
            if i!=j and i*j % 2 !=0:
                yield(i,j)


gen = product(data)
for item in gen:
    print(item)

