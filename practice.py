'''
spaces stars
3       1
2       3
1       5
0       7
1       5--->no of lines
0       7
1       5
2       3
3       1'''

n=7
spaces=n//2
stars=1
for lines in range(n//2+1):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(stars):
        print('*',end = ' ')
    print()
    spaces-=1
    stars+=2
spaces=1
stars=n-2
for lines in range(6):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(stars):
        print('*',end = ' ')
    print()
spaces,stars=0,n
for lines in range(n):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(stars):
        print('*',end = ' ')
    print()
    spaces,stars=spaces+1,stars-2
        

