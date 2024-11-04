n = int(input())

for i in range(n):
    a, b, c = map(float,input().split())
    print('$'+str(format(a*b*c,".2f")))