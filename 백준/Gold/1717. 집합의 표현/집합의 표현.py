import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find(x):
    # 경로 압축
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


n, m = map(int, input().split())
parent = list(range(n+1))

for _ in range(m):
    operation, a, b = map(int, input().split())

    if operation == 0:
        union(a,b)
    else:
        a_root = find(a)
        b_root = find(b)

        if a_root == b_root:
            print('YES')
        else:
            print('NO')
