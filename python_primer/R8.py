"""
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index
−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
the same element?
"""

string = "ABCDEFGH"
print("length of string n:",len(string)) # equals 8
"""
- k is -ve value and j is postive
- To find condition on index ie  string[-k] = string[j] 
- for example taking element F from string
"""
print(string[5])
print(string[-3])

"""soloution hint given in Textbook Study Guide: Hints to Exercises 
- Give your answer in terms of n and k.
ie string[n+k] = s[j]
taking n= 8,k=-3


 """
print(string[8+(-3)])


