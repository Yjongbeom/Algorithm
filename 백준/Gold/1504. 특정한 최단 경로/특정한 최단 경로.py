import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int ,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
    
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    return distance


start = 1
v1, v2 = map(int, input().split())

origin_distance = dijkstra(start)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = origin_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = origin_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)

if result < INF:
    print(result)
else:
    print(-1)