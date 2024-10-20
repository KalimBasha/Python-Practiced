'''num=5
for lines in range(1,num+1):
    for st in range(lines):
        print('*',end=' ')
    print()
print('----')
num=5
for lines in range(num,0,-1):
    for st in range(lines):
        print('*',end=' ')
    print()
print('----')
num,space=5,num-1
for lines in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(lines):
        print('*',end=' ')
    print()
    space-=1
print('----')
num,space=5,0
for lines in range(num,0,-1):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(lines):
        print('*',end=' ')
    print()
    space+=1
print('----')
num=4
space=num-1
for lines in range(1,num*2,2):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(lines):
        print('*',end=' ')
    print()
    space-=1
print('----')
num=9
space=num//2
star=1
for lines in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star):
        print('*',end=' ')
    print()
    if lines<num//2+1:
        space-=1
        star+=1
    else:
        space+=1
        star-=1
print('----')
num=5
for lines in range(num,0,-1):
    for n in range(lines):
        print(lines,end=' ')
    print()
print('----')
num=5
space=num-1
for lines in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for n in range(1,lines+1):
        print(n,end=' ')
    print()
    space-=1
print('----')
num=5
space=0
for lines in range(num,0,-1):
    for sp in range(space):
        print(' ',end=' ')
    for n in range(1,lines+1):
        print(n,end=' ')
    print()
    space+=1
print('----')
def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return True
print(list(map(prime,range(11,41))))
def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return num
print(list(filter(prime,range(11,41))))
var='kalim'
rev=''
for ind in range(-1,-len(var)-1,-1):
    rev+=var[ind]
print(rev)
num=5
for lines in range(num,0,-1):
    for st in range(lines):
        print('*',end=' ')
    print()
num=5
space=num//2
star=1
for lines in range(num):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star):
        print('*',end=' ')
    print()
    if lines<num//2:
        space-=1
        star+=2
    else:
        space+=1
        star-=2
num=7
space=num//2
star=1
for lines in range(num):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star):
        print('*',end=' ')
    print()
    if lines<num//2:
        space-=1
        star+=1
    else:
        space+=1
        star-=1
num=5
space=0
for lines in range(num,0,-1):
    for sp in range(space):
        print(' ',end=' ')
    for val in range(lines):
        print(lines,end=' ')
    print()
    space+=1
num=5
for lines in range(num,0,-1):
    for val in range(1,lines+1):
        print(val,end=' ')
    print()
num=6
for lines in range(num,0,-1):
    for val in range(lines,0,-1):
        print(val,end=' ')
    print()
num=5
space=num-1
for lines in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for val in range(1,lines+1):
        print(val,end=' ')
    print()
    space-=1
num=5
space=0
for lines in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for val in range(lines,num+1):
        print(val,end=' ')
    print()
    space+=1
num=7
space=0
val=num*2
for lines in range(num):
    for sp in range(space):
        print(' ',end=' ')
    for n in range(1,val):
        print(n,end=' ')
    print()
    space+=1
    val-=2
num=3
fc=0
for fa in range(1,num+1):
    if num%fa==0:
        fc+=1
if fc==2:
    print('prime')
else:
    print('not prime')
num=100
for fa in range(2,int(num**1/2+1)):
    if num%fa==0:
        print('not prime')
        break
else:
    print('prime')
num=5
fact=1
for fa in range(num,0,-1):
    fact*=fa
print(fact)
num=1234
res=0
while num!=0:
    rem=num%10
    res+=rem
    num//=10
print(res)
num=153
dup=num
res=0
p=len(str(num))
while num!=0:
    rem=num%10
    res+=rem**p
    num//=10
print('arm' if dup==res else 'not')
num=135
dup=num
res=0
p=len(str(num))
while num!=0:
    rem=num%10
    res+=rem**p
    num//=10
    p-=1
print('disarum' if dup==res else 'not')
num=6
res=0
for fa in range(1,num//2+1):
    if num%fa==0:
        res+=fa   
print('special' if num==res else 'not')
num=192
t=str(num*1)+str(num*2)+str(num*3)
for val in range(1,10):
    if str(val) not in t:
        print('not')
        break
else:
    print('fas')
num=2025
var=str(num)
a=int(var[ :len(var)//2])
b=int(var[len(var)//2: ])
res=(a+b)**2
print('tech' if res==num else 'not')
num=26
res=0
p=1
while num!=0:
    rem=num%2
    res+=rem*p
    num//=2
    p*=10
print(res)
num=13
while num>9:
    res=0
    while num!=0:
        rem=num%10
        res+=rem**2
        num//=10
    num=res
print('happy' if num==1 or num==7 else 'not')
num=23
i=0
while i*(i+1)<=num:
    if i*(i+1)==num:
        print('pronic')
        break
    i+=1
else:
    print('not')
def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return 'not'
    return 'prime'
print(prime(24))
def arm(num,p,res=0):
    while num!=0:
        rem=num%10
        res+=rem**p
        num//=10
    return res
num=153
print(arm(num,len(str(num))))
def prime(num):
    for fa in range(2,num//2+1):
        if num%fa == 0:
            return False
    return True
def pali(num,power,rev=0):
    while num!=0:
        rem=num%10
        rev+=rem*power
        num//=10
        power//=10
    return rev
num=12
power=10**(len(str(num))-1)
print('paly' if prime(num) and pali(num,power)==num else 'not')
def prime(num):
    for fa in range(2,num//2+1):
        if num%fa == 0:
            return False
    return True
def pali(num,power,rev=0):
    while num!=0:
        rem=num%10
        rev+=rem*power
        num//=10
        power//=10
    return rev
num=17
power=10**(len(str(num))-1)
revnum=pali(num,power)
print('emirp' if prime(num) and prime(revnum) and revnum!=num else 'not')
def sq(num,res=0):
    while num!=0:
        rem=num%10
        res+=rem**2
        num//=10
    return res
def happy(num):
    while num>9:
        num=sq(num)
    return num==1 or num==7
num=15
print('happy' if happy(num) else 'not')
def sunny(num,i=0):
    while i*i<=num+1:
        if i*i==num+1:
            return 'sunny'
        i+=1
    return 'not'
print(sunny(25))
def harshad(num,res=0):
    while num!=0:
        rem=num%10
        res+=rem
        num//=10
    return True if num%res==0 else False
num=22
print('harshad' if harshad(num) else 'not')
def fact(num):
    if num==1 or num==0:
        return 1
    return num*fact(num-1)
print(fact(4))
def armstrong(num,d):
    if num==0:
        return 0
    return (num%10)**d+armstrong(num//10,d)
num=153
print(armstrong(num,len(str(num))))
def armstrong(num,d):
    if num==0:
        return 0
    return (num%10)**d+armstrong(num//10,d-1)
num=135
print(armstrong(num,len(str(num))))
def prime(num,fa=2):
    if fa==num//2+1:
        return 'prime'
    elif num%fa==0:
        return 'not'
    return prime(num,fa+1)
print(prime(23))
def fact(num):
    if num==0 or num==1:
        return 1
    return num*fact(num-1)
def strong(num,res=0):
    if num==0:
        return 0
    return fact(num%10)+strong(num//10)
print(strong(145))
def b2d(num,power=1,res=0):
    if num==0:
        return 0
    return (num%10)*power+b2d(num//10,power*2)
print(b2d(1110))
def sq(num):
    if num==0:
        return 0
    return (num%10)**2+sq(num//10)
def happy(num):
    if num<10:
        return num==1 or num==7
    return happy(sq(num))
print(happy(19))
    
print(list(filter(lambda n:n%2==0,range(100,201))))
var='malayalam'
rev=var[ : :-1]
print('palindrome' if rev==var else 'not')
num=5
for lines in range(num,0,-1):
    for val in range(lines,num+1):
        print(val,end=' ')
    print()
def armstrong(num,dig):
    if num==0:
        return 0
    return (num%10)**dig+armstrong(num//10,dig)
num=153
print('armstrong' if armstrong(num,len(str(num)))==num else 'not')
from functools import reduce
print(reduce(lambda x,y:x+y,[100,200,300,400,500]))

num=908
dc=0
while num!=0:
    dc+=1
    num//=10
print(dc)

def I2B(num,pos=1):
    if num==0:
        return 0
    return (num%2)*pos+I2B(num//2,pos*10)
num=26
print(I2B(num))

num=8098770080
while num!=0:
    rem=num%10
    if rem>1:
        for fa in range(2,rem//2+1):
            if rem%fa==0:
                break
        else:
            print(rem)
    num//=10'''

