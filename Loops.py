'''
a='hii kalim basha'
for ch in a:
    print(ch)
print(ch)

lst=[12,'kalim',23,(45,67)]
for ele in lst:
    print(ele)

#print 10 natural numbers
for nat in range(1,11):
    print(nat)

#program to print all even numbers within given range
num=int(input("Enter a num:"))
for i in range(1,num):
    if (i%2==0):
        print(i)

#program to calculate the sum of all numbers from 1 to a given number
num=int(input("Enter a num:"))
c=0
for add in range(1,num+1):
    c+=add
print(c)

#program to calculate the sum of all the odd numbers within the given range
num=int(input("Enter a num:"))
c=0
for i in range(1,num):
    if i%2!=0:
        c+=i
print(c)

#program to print a multiplication table of a given number
num=int(input("Enter a num:"))
for tab in range(1,17):
    print(tab,'*', num,'=', tab*num)

# program to count the total number of digits in a number
num=input("Enter a num:")
print(len(num))

a=0
while (a<=5):
    print(a)
    a=a+1

n = int(input("Enter a Number:"))
for line in range(1,n+1):
    for st in range(line):
         print("*",end = ' ')
    print()

n = int(input("Enter a Number:"))
for line in range(n,0,-1):
    for st in range(line):
         print("*",end = ' ')
    print()

n = int(input("Enter a Number:"))
for line in range(1,n+1):
    for st in range(n):
         print("*",end = ' ')
    print()

n = int(input("Enter a Number:"))
spaces=n-1
for line in range(1,n+1):
    for sp in range(spaces):
        print(" ",end = ' ')
    for st in range(line):
         print("*",end = ' ')
    print()
    spaces=spaces-1

n = int(input("Enter a Number:"))
spaces=0
for line in range(n,0,-1):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(line):
        print("*",end = ' ')
    print()
    spaces+=1

n = int(input("Enter a Number:"))
spaces=n-1
for line in range(1,n*2,2):
    print()
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(line):
        print('*',end = ' ')
    spaces=spaces-1

n = int(input("Enter a Number:"))
spaces=0
for line in range(n*2-1,0,-2):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(line):
        print('*',end = ' ')
    spaces+=1
    print()

n=1
for line in range(1,6):
    for num in range(line):
        print(n,end= ' ')
        n+=1
    print()'''
    










