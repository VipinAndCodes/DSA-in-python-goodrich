"""
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).

"""

def readLines(filepath):
    fp=open(filepath)
    lines = []
    while True:
        try:
            line = fp.readline()
            if line == '': raise EOFError #This will not execute if the EOFError is raised, also need to remove the \n
            lines.append(line[:-1])
        except:
            for line in reversed(lines):
                print (line)
            return #This will also serve to break the infinite loop

readLines(r'test.txt')