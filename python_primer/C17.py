"""
Had we implemented the scale function (page 25) as follows, does it work
properly?
    def scale(data, factor):
        for val in data:
            val *= factor
Explain why or why not.


"""

def scale(data,factor):
    for val in data:
        val *= factor

print('Bad scaling')
data = [1,2,3,4,5]
print (data)
scale(data, 5)
print (data)

def rescale(data,factor):
    for val in range(len(data)):
        data[val] *= factor


print('Good scaling')
data = [1,2,3,4,5]
print (data)
rescale(data, 5)
print (data)

"""
Explanation: val *= factor creates a new instance of val, but doesn't change the reference to the original object in the list
data[i] changes the reference to element i, which changes the original array

"""
