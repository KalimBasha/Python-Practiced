'''#X-pattern
num=9
for out in range(num):
    for st in range(num):
        if out==st or out==num-1-st:
            print('*',end='')
        else:
            print(' ',end='')
    print()
#Hollow square pattern
num=10
for line in range(num):
    for st in range(num):
        if line==0 or line==num-1:
            print('* ',end='')
        elif st==0 or st==num-1:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
#Hollow triangle pattern
num=16
spaces=num-1
for lines in range(1,num*2,2):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(lines):
        if lines==1 or lines==num*2-1 or st==0 or st==lines-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    spaces-=1

#cross string pattern
num=input('s:')
for out in range(len(num)):
    for st in range(len(num)):
        if out==st or out==len(num)-1-st:
            print(num[st],end='')
        else:
            print(' ',end='')
    print()

#Zoho interview pattern qn
num=5
spaces=num-1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for n in range(lines,0,-1):
        print(n,end=' ')
    print()
    spaces-=1

#googly number
num=16
res=0
while num!=0:
    rem = num%10
    res += rem
    num//=10
for fa in range(2,res//2+1):
    if res%fa==0:
        print('Not Googly Number')
        break
else:
    print('Googly Number')

#sort based on 2nd ele in tuple
l=[(1,2),(3,7),(2,0)]
a=sorted(l,key=lambda x:x[1])
print(a)'''
'''
num=5
spaces=num-1
a=1
for out in range(1,num+1):
    for sp in range(spaces):
        print(' ',end='')
    for n in range(out):
        print(a,end='')
        a+=1
    print()
    spaces-=1

#replace the chr 'a' with 'p'
input1='apples'
output='paales'
res=''
for ch in input1:
    if ch=='a':
        res+='p'
    elif ch=='p':
        res+='a'
    else:
        res+=ch
print(res)

#count the no of occurences of 2nd largest integer
i=12344555
output=2
a=[]
m=0
s=0
while i!=0:
    rem=i%10
    if rem>m:
        m=rem
        s=m
    a.append(s)
    i//=10
print(a.count())

#counting characters
a='abcab'
res=''
for i in a:
    if i not in res:
        b=a.count(i)
        res+=str(b)+i
print(res)
'''
'''
#Factorial without multiplication
n=int(input('Enter a number:'))
fact,val=1,0
for fa in range(1,n+1):
    for i in range(fa):
        val+=fact
    fact=val
    val=0
print(fact)
'''

n=4
spa=n-1
for i in range(1,n+1):
    for sp in range(spa):
        print(' ',end=' ')
    for st in range(1,i+1):
        if st < i//2+1:
            for j in range(i,1,-1):
                print(j,end=' ')
        else:
            for k in range(1,i+1):
                print(k,end=' ')
    print()
    spa-=1
'''
n=4
spaces=n-1
for i in range(1,n*2,2):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(i):
        if st < i//2:
            for j in range(st,0,-1):
                print(j,end=' ')
        else:
            for k in range(1,st):
                print(k,end=' ')
    print()
    spaces-=1
'''







