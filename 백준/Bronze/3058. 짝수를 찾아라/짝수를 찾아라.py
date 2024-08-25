n = int(input())

for _ in range(n):
    mins = 9999999
    sums = 0
    num_list = list(map(int, input().split()))
    
    for num in num_list:
        if num % 2 == 0:
            mins = min(num, mins)
            sums += num
    
    print(sums, mins)