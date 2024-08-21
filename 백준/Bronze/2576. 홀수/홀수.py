num_list = []
for _ in range(7):
    n = int(input())

    if n % 2 == 1:
        num_list.append(n)

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))