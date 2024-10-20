'''
num = 5
for lines in range(1,num + 1):
    print('*',end = ' ')

num = 5
for lines in range(1,num + 1):
    for st in range(1,num + 1):
        print('*',end = ' ')
    print()

num = 5
for lines in range(1,num + 1):
    for st in range(lines):
        print('*',end = ' ')
    print()

num = 5
for lines in range(num,0,-1):
    for st in range(lines):
        print('*',end = ' ')
    print()

num = 7
spaces = num -1
for lines in range(1,num + 1):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(lines):
        print('*',end = ' ')
    print()
    spaces -=1

num = 7
spaces = 0
for lines in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(lines):
        print('*',end = ' ')
    print()
    spaces +=1

num = 7
stars = 1
for lines in range(1,num + 1):
    if lines % 2 != 0 and lines >1:
         for st in range(1,lines+1):
            print(st,end = ' ')
    else:
         for st in range(stars):
            print('*',end =' ')
    print()
    stars+=1

num = 4
spaces = num-1
stars=1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(stars):
        print('*',end = ' ')
    print()
    spaces,stars=spaces - 1,stars + 2

num = 4
spaces = 0
stars=num*2-1
for lines in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(stars,0,-1):
        print('*',end = ' ')
    print()
    spaces,stars=spaces + 1,stars - 2

num = 9
stars =num-1
spaces = num-1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end = ' ')
    if lines % 2!=0:
        for st in range(lines):
            print('*',end = ' ')
    else:
        for ts in range(num,stars,-1):
            print(ts,end=' ')  
    print()
    spaces-=1
    stars-=1

num = 9
spaces = num // 2-1
n=2
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end = ' ')
    if lines%2!=0:
        for st in range(1,n):
            print('*',end = ' ')
    else:
        for st in range(1,n):
            print(st,end = ' ')
    print()
    if lines<num//2:
        spaces-=1
        n+=2
    else:
        spaces+=1
        n-=2

num = 9
spaces=num//2
stars=1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end = ' ')
    if lines==num//2+1 :
            for st in range(stars):
                 if st%2!=0:
                    print(' ',end=' ')
                 else:
                    print('*',end=' ')
    else:
        for st in range(stars):
            print('*',end = ' ')
    print()
    if lines<num//2+1:
        spaces=spaces-1
        stars+=2
    else:
        spaces+=1
        stars-=2

num = 7
stars=1
for lines in range(1,num+1):
    for st in range(stars):
        print('*',end = ' ')
    print()
    if lines<num//2+1:
        stars+=1
    else:
        stars-=1

num = 11
spaces = num//2
stars = 1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end = ' ')
    print()
    if lines<num//2+1:
        spaces-=1
        stars+=1
    else:
        spaces+=1
        stars-=1

num = 7
spaces=num-1
stars=1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(stars):
        print('*',end = ' ')
    print()
    stars+=2
    spaces-=1'''

num = 3
spaces=0
stars=num*2-1
for lines in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(stars):
        print('*',end = ' ')
    print()
    stars-=2
    spaces+=1
