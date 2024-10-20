n=4
spaces=n-1
for line in range(1,n*2,2):
    
    for sp in range(spaces):
        print(' ',end='')
    for val in range(1,line+1):
        if val>val%2:
            for num in range(val,0,-1):
                print(num,end='')
        else:
            for num in range(1,val):
                print(num,end='')
            
    print()
    spaces-=1
