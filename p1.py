'''num=5
spaces,stars=num//2,1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    if lines<num//2+1:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2

num=5
for lines in range(num,0,-1):
    for val in range(lines,0,-1):
        print(val,end= ' ')
    print()

num=15
fc=0
for fa in range(1,num+1):
    if num%fa==0:
        fc+=1
if fc==2:
    print('prime')
else:
    print('not prime')

num=21
for fa in range(2,num//2+1):
    if num%fa==0:
        print('not prime')
        break
else:
    print('prime')

num=23
for fa in range(2,int(num**1/2)+1):
    if num%fa==0:
        print('not prime')
        break
else:
    print('prime')

num=3
fact=1
for fa in range(1,num+1):
    fact*=fa
print(fact)

num=12345
res=0
while num!=0:
    rem=num%10
    res+=rem
    num//=10
print(res)

num=12345
res=0
while num!=0:
    rem=num%10
    if rem%2==0:
       res+=rem
    num//=10
print(res)

num=12345
eres,ores=0,0
while num!=0:
    rem=num%10
    if rem%2==0:
       eres+=rem
    else:
        ores+=rem
    num//=10
print(eres,ores)

num=152
dup=num
res=0
digits=len(str(num))
while num!=0:
    rem=num%10
    res+=rem**digits
    num//=10
print(res)
if res==dup:
    print('Armstrong')
else:
    print('Not Armstrong')

num=135
dup=num
res=0
digits=len(str(num))
while num!=0:
    rem=num%10
    res+=rem**digits
    num//=10
    digits-=1
print(res)
if res==dup:
    print('Disarum')
else:
    print('Not Disarum')

num=6
fac=0
for fa in range(1,num//2+1):
    if num%fa==0:
        fac+=fa
print(fac)
if fac==num:
    print('special')
else:
    print('Not special')

num=154
dup=num
res=0
while num!=0:
    rem=num%10
    fact=1
    for fa in range(1,rem+1):
        fact*=fa
    res+=fact
    num//=10
print(res)
print('strong' if res==dup else 'not strong')

num=190
tot=str(num*1)+str(num*2)+str(num*3)
for fa in range(1,10):
    if str(fa) not in tot:
        print('Not fascinating')
        break
else:
    print('fascinating')

num=2025
var=str(num)
a=int(var[ :len(var)//2])
b=int(var[len(var)//2: ])
res=(a+b)**2
if res==num:
    print('tech')
else:
    print('Not tech')

num=26
pos=1
res=0
while num!=0:
    rem=num%2
    res+=rem*pos
    num//=2
    pos*=10
print(res)

num=11011
pos=1
res=0
while num!=0:
    rem=num%10
    res+=rem*pos
    num//=10
    pos*=2
print(res)

num=26
res=0
while num!=0:
    rem=num%2
    if rem==1:
       res+=1
    num//=2
if res%2==0:
    print('evil')
else:
    print('odeous')

num=19
while num>10:
    res=0
    while num!=0:
        rem=num%10
        res+=rem**2
        num//=10
    num=res
print('Happy' if num==1 or num==7 else 'not happy')

num=45
i=1
while i*(i+1)<=num:
    if i*(i+1)==num:
        print('pronic')
        break
    i+=1
else:
    print('not pronic')

def num(n):
    if n==11:
        return 
    print(n)
    return num(n+1)
n=1
print(num(n))

def rev(num):
    if num==0:
        return
    print(num)
    return rev(num+1)
print(rev(-11))
'''
def sq(num,res=0):
    while num!=0:
        rem=num%10
        res+=rem**2
        num//=10
    return res
def happy(num):
    while num>9:
        num=sq(num)
    return num==1 or num == 7
print(list(filter(happy,range(1,101))))
