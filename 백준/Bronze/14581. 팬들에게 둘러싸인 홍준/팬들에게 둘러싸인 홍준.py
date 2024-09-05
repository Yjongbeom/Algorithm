s = input()

for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(":", end=s + ":")
        else:
            print(":fan:", end ='')
    print()