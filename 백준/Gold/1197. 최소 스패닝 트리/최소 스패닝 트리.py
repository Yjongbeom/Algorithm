import sys

class disjointSets:
    def __init__(self, n):
        self.parent = list(range(n))
        self.set_size = n

    def find(self, id):
        if self.parent[id] != id:
            self.parent[id] = self.find(self.parent[id])
        return self.parent[id]
    
    def union(self, s1, s2):
        s1 = self.find(s1)
        s2 = self.find(s2)
        if s1 < s2:
            self.parent[s2] = s1
        else:
            self.parent[s1] = s2

def MSTKruskal(V, adj):
    n = len(V)
    dsets = disjointSets(n)

    adj.sort(key = lambda e : e[2])

    total_cost = 0
    ecount = 0
    for i in range(len(E)):
        a, b, cost = E[i][0], E[i][1], E[i][2]
        uset = dsets.find(E[i][0])
        vset = dsets.find(E[i][1])

        if uset != vset:
            dsets.union(uset, vset)
            total_cost += cost
            ecount += 1
            if ecount == n-1:
                break

    return total_cost

n, m = map(int,sys.stdin.readline().split())
V = list(range(n+1))
E = []

for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    E.append((a, b, cost))

print(MSTKruskal(V, E))