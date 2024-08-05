import sys

s = set()
n = int(sys.stdin.readline().strip())

for _ in range(n):
    order = sys.stdin.readline()

    if order.startswith("add"):
        x = int(order.split()[1])
        if x not in s:
            s.add(x)
    elif order.startswith("remove"):
        x = int(order.split()[1])
        if x in s:
            s.remove(x)
    elif order.startswith("check"):
        x = int(order.split()[1])
        if x in s:
            print(1)
        else:
            print(0)
    elif order.startswith("toggle"):
        x = int(order.split()[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif order.startswith("all"):
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif order.startswith("empty"):
        s = set()