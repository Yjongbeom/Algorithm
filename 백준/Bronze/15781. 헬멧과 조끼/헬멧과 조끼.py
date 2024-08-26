n,m = map(int, input().split())

h = list(map(int, input().split()))
j = list(map(int, input().split()))

h_max = max(h)
j_max = max(j)

print(h_max+j_max)