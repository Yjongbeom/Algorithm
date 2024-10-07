count = 0

while True:
    try:
        text = input()
        count += 1
    except EOFError :
        break;
        
print(count)