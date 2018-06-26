import math
import time
import random

def random_list(size, larger_than, smaller_than):
    list_to_sort = []
    for i in range(size):
        list_to_sort.append(random.randint(larger_than,smaller_than))
    return list_to_sort 
    
def insertion_sort(A):
    Sorted = []
    Sorted.append(A[0])
    for n in range(1, len(A)):
        if A[n] <= Sorted [0]:
           Sorted.insert(0, A[n])
        else:
            i = 0
            while (i < len(Sorted)) and (A[n] > Sorted[i]):
                i = i + 1
            Sorted.insert(i, A[n])
            
    return Sorted
#TestCase = insertion_sort([3, 5, 6, 7, 2, 3, 1, -100])
start_time = time.time()
TestCase = insertion_sort(random_list(1000, -1000, 1000))
finish_time = time.time()

print(TestCase)

print ("it took " + str(finish_time - start_time) + " seconds to sort "  + str(len(TestCase)) + " integers using insertion sort.")
