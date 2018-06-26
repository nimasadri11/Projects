import random

def randomizedSelection(A, j):
    j = j - 1
    if len(A) == 1:
        return A[0]
    elif len(A) > 1:
        wall = 0
        pIndex = random.randint(0, len(A) - 1)
        p = A.pop(pIndex)
        for i in range(0, len(A)):
            if p > A[i]:
                s = A[wall]
                A[wall] = A[i]
                A[i] = s
                wall = wall + 1
        if wall == len(A):
            A.append(p)
        else:
            q = A[wall]
            A[wall] = p
            A.append(q)
        if wall == j:
            return A[wall]
        elif wall > j:
            return randomizedSelection(A[:wall], (j + 1))
        elif j > wall:
            return randomizedSelection(A[(wall + 1):], (j - wall))

def randomList(size):
    lst = []
    for i in range(size):
        lst.append(random.randint(-1000, 1000))
    return lst
                   
test = randomList(1000)
ind = random.randint(0, len(test) - 1)
print('test: ', test)
print('ind: ', ind)
print(randomizedSelection(test, ind))                               
                                 

