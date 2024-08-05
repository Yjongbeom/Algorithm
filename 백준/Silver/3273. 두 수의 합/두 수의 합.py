import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
x = int(input())
result = []
num_list.sort()

left,right = 0, n-1
cnt = 0

while left < right:
    sums = num_list[left] + num_list[right]

    if num_list[right] + num_list[left] > x:
        right -= 1
    else:
        if sums == x:
            cnt += 1
        left += 1

print(cnt)