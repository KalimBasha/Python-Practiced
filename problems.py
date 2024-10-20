'''
#prime number(1)
num=int(input("Enter a Number:"))
print(num)
count=0
for fa in range(1,num+1):
        if num%fa==0:
            count+=1
print(count)
if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")

#(2)
num=int(input("Enter a Number:"))
print(num)
count=0
for fa in range(2,num//2+1):
        if num%fa==0:
             print(" Not Prime Number")
             break
else:
    print("Prime Number")

#(3)
num=int(input("Enter a Number:"))
print("The num is:",num)
count=0
for fa in range(2,int(num**1/2+1)):
        if num%fa==0:
             print("Not Prime Number")
             break
else:
    print("Prime Number")
    
#Factorial
num=int(input("Enter a Number:"))
fact=1
for val in range(num,0,-1):
    fact*=val
print(fact)

#Add all digits in a number
num=int(input("Enter a Number:"))
res=0
while num !=0:
        rem=num%10
        res+=rem
        num//=10
print(res)

#Add only even digits
num=int(input("Enter a Number:"))
res=0
while num!=0:
        rem=num%10
        if rem%2==0:
                res+=rem
        num//=10
print(res)

#All even & odd digits
num=int(input("Enter a Number:"))
evsum,oddsum=0,0
while num!=0:
        rem=num%10
        if rem%2==0:
                evsum+=rem
        else:
                oddsum+=rem
        num//=10
print(evsum,oddsum)

#Armstrong Number
num=153
dup=num
digits=len(str(num))
res=0
while num!=0:
        rem=num%10
        res+=rem**digits
        num//=10
print(res)
if dup==res:
        print('Armstrong')
else:
        print('Not Armstrong')
      
#Disarum Number
num=135
dup=num
digits=len(str(num))
res=0
while num!=0:
        rem=num%10
        res+=rem**digits
        num//=10
        digits-=1
print(res)
if dup==res:
        print('Disarum Number')
else:
        print('Not Disarum Number')

#Special Number
num=6
res=0
for fa in range(1,num//2+1):
        if num%fa==0:
                res+=fa
print(res)
if num==res:
        print('Special Number')
else:
        print('Not Special Number')

#Strong Number
num=145
dup=num
res=0
while num!=0:
        rem=num%10
        fact=1
        for fa in range(rem,0,-1):
                fact*=fa
        res+=fact
        num//=10
print(res)
if dup==res:
        print('Strong')
else:
        print('Not Strong')

#Fascinating Number
num=193
tot=str(num*1)+str(num*2)+str(num*3)
for val in range(1,10):
        if str(val) not in tot:
                print('Not Fascinating')
                break
else:
        print('Fascinating')

#Tech Number
num = 2025
var=str(num)
a=int(var[ :len(var)//2])
b=int(var[len(var)//2: ])
res=(a+b)**2
if num==res:
        print('Tech Number')
else:
        print('Non Tech Number')
'''
