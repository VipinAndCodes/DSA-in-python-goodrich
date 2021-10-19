
"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""


def minmax(data):
    #len of data !=0
    if len(data):
        min=max=data[0]
        for value in data:
            if value > max: max = value
            elif value < min: min = value
        return (min,max)
    else:
        print("please enter a valid data")

print(minmax([6,2,8,7,3,1])) 
                
            



    
