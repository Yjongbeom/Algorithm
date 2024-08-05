s = input().strip()
bomb = list(input())

arr = []

for i in range(len(s)):
    arr.append(s[i])
    if arr[-len(bomb):] == bomb:
        del arr[-len(bomb):]
        
if arr:
    for ch in arr:
        print(ch, end = '')
else:
    print("FRULA")