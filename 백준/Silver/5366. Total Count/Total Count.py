import sys
input = sys.stdin.readline

dicts = {}

while True:
    s = input().strip()

    if s == '0':
        break

    if s not in dicts:
        dicts[s] = 1
    else:
        dicts[s] += 1

    
for num in dicts:
    print(f'{num}: {dicts[num]}')

print(f'Grand Total: {sum(dicts.values())}')