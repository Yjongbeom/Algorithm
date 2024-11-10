n,a= int(input()),list(map(int,input().split()))
count= 0
for i in range(n):
    if a[i] % 2 == 0:
        count += 1

print("Happy" if count > n/2 else "Sad")