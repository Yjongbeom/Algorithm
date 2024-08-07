import sys
input = sys.stdin.readline

n, m = map(int ,input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

left, right = 1, max(arr)

while left <= right:
    mid = (left + right) // 2
    length = 0
    
    for i in arr:
        length += i // mid
            
    if length >= m:
        left = mid + 1
        
    else:
        right = mid - 1
    
print(right)