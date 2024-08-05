import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
result = []
min = 2000000000

num_list.sort()
left,right = 0, n-1
min_l, min_r = 0, 0

while left < right:
    sums = num_list[left] + num_list[right]

    if abs(sums) < min:
        min = abs(sums)
        min_l = num_list[left]
        min_r = num_list[right]

    if min == 0:
        break

    if abs(num_list[left]) < abs(num_list[right]):
        right -= 1
    else:
        left += 1

print(min_l, min_r)