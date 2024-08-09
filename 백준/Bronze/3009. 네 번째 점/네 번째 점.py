x_l = []
y_l = []

for _ in range(3):
    x, y = map(int, input().split())
    x_l.append(x)
    y_l.append(y)
    
for i in range(3):
    if x_l.count(x_l[i]) == 1:
        x = x_l[i]
    if y_l.count(y_l[i]) == 1:
        y = y_l[i]
        
print(x, y)