''''
sources: https://www.geeksforgeeks.org/disjoint-set-data-structures/ , 
Using the disjount data structure from the exploration in the Kruskals algorithm section
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

    MST = set()

    ds_set = DisjSet(V)

    print("Edge : Weight")
    for (u, v, w) in e_sorted:
        if ds_set.Find(u) != ds_set.Find(v):
            MST.add((u,v))
            ds_set.Union(u,v)
            print(str(u) + "-" + str(v) + ": " + str(w))


ex = [[0,9,75,0,0],[9,0,95,19,42],[75,95,0,51,66],[0,19,51,0,31],[0,42,66,31,0]]
kruskals(ex)
