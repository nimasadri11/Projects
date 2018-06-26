import math
import random

def ClosestPair(A):

    # returns distance in the form of (point1, point2, distance)
    def distance(P, Q):
        Soln = []
        Soln.append(P)
        Soln.append(Q)
        Soln.append(math.sqrt((((P[0]) - (Q[0])) ** 2) + (((P[1]) - (Q[1])) ** 2)))
        return Soln


    # Pre-processing step
    def Pre(Array):
        def get_2nd(element):
            return element[1]
        def get_1st(element):
            return element[0]
        # sorting occurding to x and y coordinates
        X = sorted(Array, key=get_1st)
        Y = sorted(Array, key=get_2nd)
        return [X, Y]


    # Recursive calls
    def Process(W):
        X = W[0]
        Y = W[1]
        distance_points = []
        
        # for split points
        def SplitClosestPair(Z):
            x = Z[0]
            y = Z[1]
            min_dis = Z[2]
            first = min_dis[0]
            second = min_dis[1]
            x_mid = x[math.ceil(len(x)/2)]
            strip = []
            smallest = min_dis

            # checks to see if the point lies inside the strip (result would be sorted by y-cordinate) 
            for e in y:
                if (abs(x_mid[0] - e[0]) <= min_dis[2]):
                    strip.append(e)
            
            # checks if any 2 points in "strip" have a distance that is less than the distance previosly calculates
            for s in range(0, len(strip)):
                for t in range(1, min(7, len(strip)-s)):
                    length = distance(strip[s], strip[s + t])
                    if smallest[2] > length[2]:
                        smallest = length
            return smallest


        # base case
        if len(X) <= 3:
            for p in X:
                X.remove(p)
                for q in X:
                    distance_points.append(distance(p, q))
            return min(distance_points)

            
        # recursive call for the left side
        else:
            mid = int(math.ceil(len(X)/2))
            left_X = X[:mid]
            right_X = X[mid:]
            left_Y = Y[:mid]
            right_Y = Y[mid:]
            min_left = Process([left_X, left_Y])
            min_right = Process([right_X, right_Y])
            if min_right[2] >= min_left[2]:
                min_left_and_right = min_left
            else:
                min_left_and_right = min_right
            return SplitClosestPair([X, Y, min_left_and_right])
    return Process(Pre(A))

def random_points(num):
    theList = []
    for i in range(num):
        x = random.uniform(-1000.1, 1000.1)
        y = random.uniform(-1000.1, 1000.1)
        theList.append([x, y])
    return theList
        
test = random_points(1000)
print(test)
print(ClosestPair(test))
