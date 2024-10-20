'''
#first 15 armstrong numbers
def armstrong(num,digits):
    res=0
    while num!=0:
        rem=num%10
        res+=rem**digits
        num//=10
    return res
n=0
num=0
while n != 15:
    if armstrong(num,len(str(num)))==num:
        print(num)
        n+=1
    num+=1
'''  
'''
#swapping two elements
a=20
b=30

#m-1
a,b=b,a
print(a,b)

#m-2
c=a
a=b
b=c
print(a,b)

#m-3
a=a+b
b=a-b
a=a-b
print(a,b)
'''
'''
#pattern in python
word=input('Enter a string:')
spaces=len(word)-1
for i in range(-1,-len(word)-1,-1):
    for sp in range(spaces):
        print(' ',end='')
    for ch in range(-1,i-1,-1):
        print(word[ch],end='')
    print()
    spaces-=1
'''
'''
#hollow pattern prgrm
n=int(input("Enter a number:"))
spaces=n-1
for i in range(1,n*2,2):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(i):
        if(i==1 or i==n*2-1):
            print('*',end='')
        else:
            if(st==0 or st==i-1):
                print('*',end='')
            else:
                print(' ',end='')
    spaces-=1
    print()
'''
'''
#sorting binary
def binary(num):
    res=''
    while num!=0:
        rem=num%2
        res=str(rem)+res
        num//=2
    result=int(res)

    count=0
    while result != 0:
        rem=result%10
        if rem==1:
            count+=1
        result//=10
    return count,i

n1=int(input('Enter starting range:'))
n2=int(input('Enter ending range:'))
l=[]
for i in range(n1,n2+1):
    l.append(binary(i))
for ind1 in range(len(l)-1,-1,-1):
    for ind2 in range(ind1):
        if l[ind2]>l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
for a,b in l:
    print(b)
'''
'''
#adding twolists
l1=[3,5,7]
l2=[14,16,19]
print(l1+l2)
'''
'''
#dictionary
d1={'a':20,'b':30}
d2={'c':20,'a':40,'b':50}
d={}
for ele in d1.items():
    if ele[0] not in d:
        d[ele[0]]=[ele[1]]
    else:
        d[ele[0]]+=[ele[1]] 
for ele in d2.items():
    if ele[0] not in d:
        d[ele[0]]=[ele[1]]
    else:
        d[ele[0]]+=[ele[1]] 
print(d)
'''
'''
#name score
name=input('Enter your name:').upper()
print(name)
score=0
for ch in name:
    score+=ord(ch)-64
print(f'Your score is {score})
'''
'''
#adding two matrix
m1=[[1,4,5],[4,9,6]]
m2=[[8,4,2],[2,5,3]]
if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
    for r in range(len(m1)):
        for c in range(len(m1[0])):
            m1[r][c]=m1[r][c]+m2[r][c]
    print(m1)
'''
'''
#adding without arithmetic operators
a=8
b=2
while b!=0:
    c = a & b
    a = a ^ b
    b = c << 1
print(a)
'''

#longest palindrome in a string
s=input('Enter a string:')
st=0
end=-1
res=''
while st != len(s):
    if s[st]==s[end]:
        res+=s[st]
    st+=1
    end-=1
print(res)




    
