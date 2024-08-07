import sys
input = sys.stdin.readline

n, m = map(int ,input().split())
arr = list(map(int, input().split()))
left, right = 1, max(arr)

while left <= right:
    mid = (left + right) // 2
    length = 0
    
    for i in arr:
        if mid <= i:
            length += i - mid
            
    if length >= m:
        left = mid + 1
        
    else:
        right = mid - 1
    
print(right)