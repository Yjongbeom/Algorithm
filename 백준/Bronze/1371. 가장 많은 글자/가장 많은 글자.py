import sys

text = sys.stdin.read()
text = text.replace('\n', '').replace(' ', '')

arr = [0 for i in range(26)]
        
for i in range(len(text)):
    arr[ord(text[i])-97] += 1

maxs = max(arr)

for i in range(len(arr)):
    if maxs == arr[i]:
        print(chr(97+i), end ='')