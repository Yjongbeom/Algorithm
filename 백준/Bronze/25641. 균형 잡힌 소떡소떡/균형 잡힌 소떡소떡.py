N = int(input())
stst = input()
lst = list(reversed(stst)) 

while 1 :
    if lst.count('s') == lst.count('t') :  
        break
    else :
        lst.pop(-1) 

lst.reverse() 
print(''.join(lst))
