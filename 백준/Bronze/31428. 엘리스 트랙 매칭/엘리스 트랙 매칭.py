n = int(input())
arr = list(input().split())
s = input()
cnt = 0
for ch in arr:
    if ch == s:
       cnt += 1
       
print(cnt) 