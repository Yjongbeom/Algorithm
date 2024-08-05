import sys

n = int(sys.stdin.readline())
res = 0
graph = []
stack = []

for _ in range(n):
    graph.append(int(sys.stdin.readline()))
graph.append(0)

stack.append((0, graph[0]))
left = 0

for i in range(1, n+1):
    left = i
    while stack and stack[-1][1] > graph[i]:
        left, h = stack.pop()
        res = max(res, (i-left)*h)
    stack.append((left, graph[i]))

print(res)