s = input()
arr = []
for i in range(len(s)):
    arr.append(s[i])

sets = set()
for i in range(len(arr)):
    s = arr[i]
    sets.add(s)
    for j in range(i, len(arr)):
        if i != j:
            s += arr[j]
            sets.add(s)

print(len(sets))
