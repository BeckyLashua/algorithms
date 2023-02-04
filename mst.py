''''
sources: https://www.geeksforgeeks.org/disjoint-set-data-structures/ , 
Using the disjount data structure from the exploration in the Kruskals 
algorithm section
Using inspiration from the Prim's brute force code solution in the Prim's 
section exploration
'''

class DisjSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def Find(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    def Union(self, x, y):
        xset = self.Find(x)
        yset = self.Find(y)

        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

def kruskals(G):
    edge_list = []
    V = len(G)
    for i in range(V):
        for j in range(V):
            if G[i][j] > 0:
                edge_list.append((i, j, G[i][j]))

    e_sorted = sorted(edge_list, key=lambda tup: tup[2])

    MST = [[0 for x in range(V)] for y in range(V)]
    ds_set = DisjSet(V)

    for (u, v, w) in e_sorted:
        if ds_set.Find(u) != ds_set.Find(v):
            ds_set.Union(u,v)
            MST[u][v] = w
            MST[v][u] = w

    return MST


def prims(G):
    V = len(G)

    MST = [[0 for x in range(V)] for y in range(V)]

    selected = [0] * V
    selected[0] = True
    edges = 0

    while edges < (V - 1):
        minimum = float('inf')
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]) > 0:
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x, y = i, j
        selected[y] = True
        edges += 1
        MST[x][y] = G[x][y]
        MST[y][x] = G[x][y]
    
    return MST

ex = [[0,9,75,0,0],[9,0,95,19,42],[75,95,0,51,66],[0,19,51,0,31],[0,42,66,31,0]]
print(kruskals(ex))
print(prims(ex))
ex_2 = [[0,2,3,0,0],[2,0,1,3,2],[3,1,0,0,1],[0,3,0,0,5],[0,2,1,5,0]]
print(kruskals(ex_2))
print(prims(ex_2))