import sys
sys.setrecursionlimit(10 ** 5)

def dfs(graph, start, visited, temp):
    global count
    visited.add(start)
    temp[start] = count
    count += 1
    nbr = sorted(list(graph[start] - visited), reverse=True)
    for v in nbr:
        if v not in visited:
            dfs(graph, v, visited, temp)
                
n, m, r = map(int, input().split())
graph = {}
global count
count = 1
temp = [0] * (n+1)

for i in range(1, n+1):
    graph[i] = set()
    
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
    
dfs(graph, r, set(), temp)

for i in range(1, n+1):
    print(temp[i])