import random


def quickSort(A):

    if len(A) == 1:
        return A
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
    if wall == len(A):
        return quickSort(A[:wall])
    elif wall == 0:
        return quickSort(A[:(wall + 1)]) + quickSort(A[wall + 1:])
    else:
        return quickSort(A[:(wall)]) + quickSort(A[wall:])


def randomList(size):
    lst = []
    for i in range(size):
        lst.append(random.randint(-1000, 1000))
    return lst


test = randomList(5000)
print(quickSort(test))
