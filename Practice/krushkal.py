class DSU:
    """ Disjoint Set Union (Union-Find) with Path Compression """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  

    def find(self, x):
        """ Find the representative of a set with path compression """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        """ Union by rank to keep tree balanced """
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True  
        return False 

def kruskal(n, edges):
    """ Kruskal’s Algorithm to find Minimum Cost Spanning Tree (MCST) """
    dsu = DSU(n)  
    min_cost = 0
    mst_edges = []

    edges.sort(key=lambda x: x[2])  

    for u, v, weight in edges:
        if dsu.union(u, v):  
            min_cost += weight
            mst_edges.append((u, v, weight))

        if len(mst_edges) == n - 1:
            break

    return min_cost, mst_edges

edges = [
    (0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2),
    (2, 3, 4), (3, 4, 2), (4, 5, 6), (3, 5, 3)
]

n = 6  

min_cost, mst = kruskal(n, edges)

print("Minimum Cost of Spanning Tree:", min_cost)
print("Edges in MST:", mst)
