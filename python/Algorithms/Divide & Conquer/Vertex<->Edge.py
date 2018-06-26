

# converts the vertex version of the graph to the edge version
def Vertex_to_Edge(V):
    E = []
    for i in range(len(V)):
        if V[i] != []:
            for node in V[i]:
                E.append([i, node])
                V[node].remove(i)
    return E


# converts the edge version of the graph to the vertex version
def Edge_to_Vertex(E):
    # --------------------------------------------------------------------------
    def makeVertecies(A):
        lst = []

        # ----------------------------------------------------------------------
        # used to find the number of vertecies; this is then used to generate the list of lists.
        def maximum(P):

            # used to get the first and second elements of the lists that are in lists
            def get_1st(element):
                return element[0]

            def get_2nd(element):
                return element[1]

            first = max(A, key=get_1st)[0]
            second = max(A, key=get_2nd)[1]

            # returns the maximum value present in the lists of lists
            return max(first, second)
        # ----------------------------------------------------------------------
        maxValue = maximum(A)
        for i in range(maxValue + 1):
            lst.append([])
        return lst
    # --------------------------------------------------------------------------
    V = makeVertecies(E)
    print("V: ", V)
    for e in E:
        V[e[0]].append(e[1])
        V[e[1]].append(e[0])
    return V
