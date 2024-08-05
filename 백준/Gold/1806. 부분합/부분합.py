import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
min_length = 100001
current_sum = 0

while right <= n:
    if current_sum >= m:
        min_length = min(min_length, right - left)
        current_sum -= arr[left]
        left += 1
    else:
        if right == n:
            break
        current_sum += arr[right]
        right += 1

if min_length > 100000:
    print(0)
else:
    print(min_length)