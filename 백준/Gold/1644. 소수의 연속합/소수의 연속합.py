import sys
import math
input = sys.stdin.readline

n = int(input())

num_list = [True] * (n+1)
num = []

if int(math.sqrt(n)+1) <= 2 and n != 1:
   num.append(n) 
elif n == 1:
    num.append(0)
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if num_list[i] == True:
            for j in range(i+i, n+1, i):
                num_list[j] = False
                
    for i in range(2, len(num_list)):
        if num_list[i] == True:
            num.append(i)
    
left, right = 0, 0
sum = 0
cnt = 0

while right <= len(num):
    if sum <= n:
        if sum == n:
            cnt += 1
        if right == len(num):
            break
        sum += num[right]
        right += 1
    else:
        sum -= num[left]
        left += 1
        
print(cnt)