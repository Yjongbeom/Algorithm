import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b, c, d = input().split()

    arr.append([a,int(b),int(c),int(d)])

arr = sorted(arr, key=lambda x : (-x[1],x[2],-x[3],x[0]))

for name, s1, s2, s3 in arr:
    print(name)