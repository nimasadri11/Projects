# Library used to ceil in the case of an array with an odd number of elements (math.ceil)
import math
import time
import random


def Merge(L, R):
    # i is the index for L, j is the index for R
    Merged = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        # From smallest to largest in L and R, it adds the smallest of them to the Merged array
        if L[i] <= R[j]:
            Merged.append(L[i])
            i = i + 1
        else:
            Merged.append(R[j])
            j = j + 1
    # Checks if the elemets in L or R have been all added to A, in which case it adds the rest of the elements of the other array to A
    if i == len(L):
        Merged.extend(R[j:])
    elif j == len(R):
        Merged.extend(L[i:])
    return Merged


def MergeSort(A):
    # base case
    if len(A) == 1:
        return A
    # recursive calls

    else:
        mid = int(math.ceil(len(A) / 2))
        # if length of the array is odd, left_half would have one element more than right_half
        left_half = A[:mid]
        right_half = A[mid:]
        # Merging the two halves
        return Merge(MergeSort(left_half), MergeSort(right_half))

# generates a random list to sort


def random_list(size, larger_than, smaller_than):
    list_to_sort = []
    for i in range(size):
        list_to_sort.append(random.randint(larger_than, smaller_than))
    return list_to_sort


# calculates the running time of Merge Sort
start_time = time.time()
TestCase = MergeSort(random_list(1000, -1000, 1000))
finish_time = time.time()

print(TestCase)
print("it took " + str(finish_time - start_time) + " seconds to sort " +
      str(len(TestCase)) + " integers using merge sort.")
