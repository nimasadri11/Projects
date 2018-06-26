import math
import random

def binarySearch(sortedArray, lookingFor):

    if len(sortedArray) == 1:
        if sortedArray[0] == lookingFor:
            return [True]
        else:
            return False 
    else:
        mid = math.ceil(len(sortedArray)/2)
        if sortedArray[mid] == lookingFor:
            return True
        elif sortedArray[mid] > lookingFor:
            return binarySearch(sortedArray[:mid], lookingFor)
        else:
            sortedArray[mid] < lookingFor
            return binarySearch(sortedArray[mid:], lookingFor)

def generateRandomArray(size):
    randomArray = []
    for i in range(size):
        randomArray.append(random.randint(-100, 100))
    return randomArray


