"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators 

"""



# The function expected to take int and raise a asseration error if value is not a integer
def is_even(k:int):
    assert type(k) == int ,"Please enter a integer"
    return (k&1 == 0)


#another method

def check_even(k):
    try: 
        return (k&1 == 0) 
    except Exception: 
        return "Number must be Integer values"



print(is_even(4))
print(is_even(50))
print(is_even(7))
print("///////////////////")
print(check_even(4))
print(check_even("k"))
print(check_even(7.5))