"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).

"""

num=[1,3,3,2,4,5,6]
num2=[1,3,2,4,5,6]

def unique(data):
    num_set=set()
    for i in data:
        if i in num_set: return False
        else: num_set.add(i) 
    return True

print(unique(num))
print(unique(num2))

###################################################

def unique_num(arr):
    set_num= set(arr)
    return len(set_num) == len(arr)

print(unique_num(num))
print(unique_num(num2))
