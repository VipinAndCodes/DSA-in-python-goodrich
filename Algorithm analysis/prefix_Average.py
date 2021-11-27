

def prefix_average1(s):
    n=len(s)
    A = [0]*n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += s[i]
            A[j] = total / (j+1)
    return A

def prefix_average2(s):
    n=len(s)
    A = [0]*n
    for j in range(n):
        A[j] = sum(s[0:j+1]) / (j+1)
    return A

def prefix_average3(s):
    n=len(s)
    A = [0]*n
    total = 0
    for j in range(n):
        total += s[j]
        A[j] = total/(j+1)
    return A



k=[1,2,3,4,5]

print(prefix_average1(k))
print(prefix_average2(k))
print(prefix_average3(k))

