'''
#reverse a string

s='kalim'
res=s[::-1]
print(res)

r=' '
for i in s:
    r=i+r
print(r)


#even or odd
n=int(input('enter:'))
if n%2==0:
    print('even')
else:
    print('odd')

#printing all factors of a number
n=int(input('enter:'))
for i in range(1,n+1):
    if n%i==0:
        print(i)

#factorial
n=int(input('enter:'))
fact=1
if n<=1:
    print(1)
else:
    for i in range(1,n+1):
        fact*=i
    print(fact)

#swapping without temporary variable
a=int(input('Enter:'))
b=int(input('Enter:'))
print('Before Swapping','a:',a,'b:',b)
a=a+b
b=a-b
a=a-b
print('After Swapping','a:',a,'b:',b)

a=int(input('Enter:'))
b=int(input('Enter:'))
print('Before Swapping','a:',a,'b:',b)
a,b=b,a
print('After Swapping','a:',a,'b:',b)

#palindrome
s=input('Enter:')
res=s[::-1]
if s==res:
    print('palindrome')
else:
    print('Not Palindrome')

s=input('Enter:')
r=''
for ch in range(len(s)-1,-1,-1):
    r+=s[ch]
if s==r:
    print('palindrome')
else:
    print('Not Palindrome')

#adding all elements in list
l=[12,1,4,6,33]
sums=0
for ele in l:
    sums+=ele
print(sums)

#prime
n=int(input('Enter:'))
for fa in range(2,int(n**(1/2)+1)):
    if n%fa==0:
        print('Not Prime')
        break
else:
    print('Prime')
    
#add all digits
n=int(input('Enter:'))
res=0
while n !=0:
    res+=n%10
    n//=10
print(res)

#add even and odd separately
n=int(input('Enter:'))
ec,oc=0,0
while n != 0:
    rem=n%10
    if rem%2==0:
        ec+=rem
    else:
        oc+=rem
    n//=10
print(ec,oc)

#armstrong
n=int(input('Enter:'))
dig=len(str(n))
dup=n
res=0
while n != 0:
    rem=n%10
    res+=rem**dig
    n//=10
if res==dup:
    print('Armstrong')
else:
    print('Not Armstrong')

#Disarum
n=int(input('Enter:'))
dig=len(str(n))
dup=n
res=0
while n != 0:
    rem=n%10
    res+=rem**dig
    n//=10
    dig-=1
if res==dup:
    print('DisArum')
else:
    print('Not disarum')

#Special
n=int(input('Enter:'))
res=0
for fa in range(1,n//2+1):
    if n%fa==0:
        res+=fa
if res==n:
    print('Special or Perfect')
else:
    print('Not Special')

#Strong
n=int(input('Enter:'))
dup=n
res=0
while n != 0:
    rem=n%10
    fact=1
    for fa in range(1,rem+1):
        fact*=fa
    res+=fact
    n//=10
if res==dup:
    print('Strong')
else:
    print('Not Strong')

#Fascinating
n=int(input('Enter:'))
s=str(n*1)+str(n*2)+str(n*3)
for num in range(1,10):
    if str(num) not in s:
        print('Not Fascinating')
        break
else:
    print('Fascinating')

#Tech Number
n=int(input('Enter:'))
s=str(n)
a=int(s[:len(s)//2])
b=int(s[len(s)//2:])
res=(a+b)**2
if n==res:
    print('Tech Number')
else:
    print('Not Tech Number')

#integer to binary
n=int(input('Enter:'))
res=0
pos=1
while n :
    rem=n%2
    res=res+rem*pos
    n//=2
    pos*=10
print(res)

#binar to integer
n=int(input('Enter:'))
res=0
pos=1
while n:
    rem=n%10
    res+=rem*pos
    n//=10
    pos*=2
print(res)

#happy
n=int(input('Enter:'))
while n > 9:
    res=0
    while n:
        rem=n%10
        res+=rem**2
        n//=10
    n=res
if n==1 or n==7:
    print('Happy Number')
else:
    print('not')
'''
'''
#Recursion
def inc(n):
    if n==10:
        return
    print(n)
    inc(n+1)
inc(0)

#Factorial
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
print(factorial(6))

#armstrong
def arm(n,dig):
    if n==0:
        return 0
    return (n%10)**dig+arm(n//10,dig)
num=1534
if arm(num,len(str(num)))==num:
    print('armstrong')
else:
    print('not')

#reverse a number
def reverse(n,dig):
    if n==0:
        return 0
    return (n%10)*(10**dig)+reverse(n//10,dig-1)
num=45678
print(reverse(num,len(str(num))-1))

#binary to integer
def b2i(n,pos=1):
    if n==0:
        return 0
    return (n%10)*pos+b2i(n//10,pos*2)
num=100
print(b2i(num))

#integer to binary
def i2b(n,pos=1):
    if n==0:
        return 0
    return (n%2)*pos+i2b(n//2,pos*10)
num=2
print(i2b(num))
'''
#creatng a matrix
'''
r=int(input('Enter:'))
c=int(input('Enter:'))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        l.append(int(input('Enter:')))
    m.append(l)
print(m)

#Adding Matrix
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,2,3],[4,5,6],[7,8,9]]
if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j]=m1[i][j]+m2[i][j]
    print(m1)
else:
    print('Not possible')

#Subtracting Matrix
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,2,3],[4,5,6],[7,8,9]]
if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j]=m1[i][j]-m2[i][j]
    print(m1)
else:
    print('Not possible')

#Multiply Matrix
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,2,3],[4,5,6],[7,8,9]]
m=[]
if len(m1[0])==len(m2):
    for i in range(len(m1)):
        line=[]
        for j in range(len(m2[0])):
            ans=0
            for v in range(len(m1)):
                ans+=m1[i][v]*m2[v][j]
            line.append(ans)
        m.append(line)
    print(m)
else:
    print('not possible')

#Transpose a matrix
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[]
for i in range(len(m1)):
    line=[]
    for j in range(len(m1[0])):
        line.append(m1[j][i])
    m2.append(line)
for x in m2:
    print(x)

#2nd most occured string in array
s=input('Enter :')
d={}
for i in s.split():
    if i in d:
        d[i]+=1
    else:
        d[i]=1
l=sorted(d,key=d.get,reverse=True)
print(l[1])
'''
'''
def decorat(args):
    def inner(l):
        l2=[]
        for i in l:
            if str(i).isdigit():
                l2.append(int(i))
        return args(l2)
    return inner

@decorat
def maxval(l):
    maxval1=l[0]
    for i in range(len(l)):
        if l[i]>maxval1:
            maxval1=l[i]
    return maxval1

l=[10,5,8,15,'kalim','90']
print(maxval(l))
'''

#AgilePoint Interview Questions
'''
#1.Reverse a String
s=input('Enter a string:')
res=''
for ch in s:
    res=ch+res
print(res)

#2.Prime numbers in range
def prime(n):
    if n>1:
        for fa in range(2,n//2+1):
            if n%fa==0:
                return False
        else:
            return True
n1=int(input('Enter starting range:'))
n2=int(input('Enter ending range:'))
print(list(filter(prime,range(n1,n2))))

#3.Sorting
def quick(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=[val for val in l[1:] if val < pivot]
    right=[val for val in l[1:] if val >= pivot]
    return quick(left)+[pivot]+quick(right)

l=[12,8,-67,2,0,-8]
print(quick(l))

#4.Fibonacci Series
#without recursion
n=int(input('Enter a range:'))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c

#with recursion
n=int(input('Enter a range:'))
def fib(n,a=0,b=1):
    if n==0:
        return
    print(a)
    c=a+b
    fib(n-1,a=b,b=c)

fib(n)

#in a given range
n1=int(input('Enter starting range:'))
n2=int(input('Enter ending range:'))
a=0
b=1
for i in range(n2):
    c=a+b
    if n1 <= c and n2 >= c:
        print(c)
    a=b
    b=c

#5.Finding Maximum in a list using Decorator
def invalid(arg):
    def inner(l):
        l1=[]
        for val in l:
            if str(val).isdigit():
                l1.append(int(val))
        return arg(l1)
    return inner

@invalid
def highest(l):
    high=0
    for ele in l:
        if high < ele:
            high=ele
    return high
l=[12,97,'102',86,'kalim','507']
print(highest(l))

a=[1,2,3,4,5]
print(''.join(['Even' if val%2==0 else 'Odd' for val in a]))

l=[9,9,8,10,12,6,14,4]
a=[]
for i in l:
    for j in l:
        if i>j and i+j==18:
            a.append((i,j))
print(max(a))
'''
n=7
spaces=n-2
k=n-1
for i in range(1,n+1):
    if(i==1 or i==n):
        for j in range(1,n+1):
            print(j,end='')
        print()
    else:
        for sp in range(spaces):
            print(' ',end='')
        print(k)
        spaces-=1
        k-=1
        print()
    

    


