import random

def random_list(size, larger_than, smaller_than):
    list_to_sort = []
    for i in range(size):
        list_to_sort.append(random.randint(larger_than,smaller_than))
    return list_to_sort
print(random_list(1000, -1000, 1000))
