s = input()
ch_list = list(input().split())

for ch in s:
    if ch in ch_list:
        print(ch.lower(),end='')
    else:
        print(ch, end='')