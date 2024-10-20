'''
#reverse a string
s='kalim'
rev=s[ : :-1]
print(rev)

s='kalim'
rev=''
for ch in s:
    rev=ch+rev
print(rev)

s='kalim'
rev=''
for i in range(-1,-len(s)-1,-1):
    rev+=s[i]
print(rev)

s='kalim'
rev=''
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print(rev)

#palindrome
s='madam'
rev=''
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print('palindrome' if rev==s else 'not')

s='maam'
rev=''
for i in range(0,len(s)//2):
    if s[i]!=s[-i-1]:
        print('not')
        break
else:
    print('palindrome')

var='malay'
s=0
e=-1
while s==len(var)//2:
    if var[s]!=var[e]:
        print('no')
        break
    s+=1
    e-=1    
else:
    print('palindrome')

var='malayalam'
count=0
for ch in var:
    if ch in 'aeiouAEIOU':
        count+=1
print(count)

#converting to upper
s='engineering'
res=''
for ch in s:
    if ch not in res:
        res+=ch
print(res)

s='engineering'
res=''
for ch in s:
    res+=chr(ord(ch)-32)
print(res)

#converting to lower
s='ENGINEERINGa234'
res=''
for ch in s:
    if ch.isupper():
        res+=chr(ord(ch)+32)
print(res)

#swapcase
s='ENGINEERINGa234'
res=''
for ch in s:
    if ch.isupper():
        res+=chr(ord(ch)+32)
    if ch.islower():
        res+=chr(ord(ch)-32)
print(res)

#print only strings
l=[420,510,True,'ashwini mam',4+4j,'123',(4.4,),{4:54,3:23},'nothing']
l1=[]
for ch in l:
    if type(ch)==str:
        l1.append(ch)
print(l1)

#print elements present in even index
l=[420,510,True,'ashwini mam',4+4j,'123',(4.4,),{4:54,3:23},'nothing']
l1=[]
for i in range(len(l)):
    if i%2==0:
        l1.append(l[i])
print(l1)

#print all no from string
var='kalim2020786'
res=''
for ch in var:
    if ch.isdigit():
        res+=ch
print(res)

#print all alphabets from string
var='kalim2020786park'
res=''
for ch in var:
    if ch.isalpha():
        res+=ch
print(res)

#print all special characters from string
var='kalim2020 @ # $ %786park'
res=''
for ch in var:
    if not ch.isalnum():
        res+=ch
print(res)

#replace
s='hi how are you?'
print(s.replace('how','who'))
res=s.split()
s1=''
for ch in res:
    if ch=='how':
        s1+='who'+' '
    else:
        s1+=ch+' '
print(s1)

s=input('Enter a string:')
s1=''
for ch in s:
    if ch in 'aeiouAEIOU':
        s1+='*'
    else:
        s1+=ch
print(s1)

#print - if occurs more than one
var='hello'
res=''
for ch in var:
    if var.count(ch)>1:
        res+='-'
    else:
        res+=ch
print(res)

#to get extension
get=input('Enter a filename:')
res=get.split('.')
print(res[-1])

#string to list and viceversa
s='hii there'
l1=list(s)
print(l1)
print(''.join(l1))
s1=''
for ch in l1:
    s1+=ch
print(s1)

#sep by using commas
var='hello welcome to python'
print(','.join(var))

#to find ascii values
var='hello'
for ch in var:
    print(ord(ch))
#to get op in tuple
print(tuple(map(lambda x:ord(var[x]),range(len(var)))))

#sum all numbers
var='sony12india567pvt21td'
res=0
for ch in var:
    if ch.isdigit():
        res+=int(ch)
print(res)

#count white spaces
var='hii hello welcome to     python'
c=0
for ch in var:
    if ch==' ':
        c+=1
print(c)

#count caps&small letters separately
var='EnGGinEEring'
caps,small=0,0
for ch in var:
    if ch.isupper():
        caps+=1
    elif ch.islower():
        small+=1
print(f'Count of caps letters is {caps}')
print(f'Count of small letters is {small}')
'''
