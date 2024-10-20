'''
name='kalim'
print(list(enumerate(name)))

name='kalim'
print([ch for ch in name])

var='get p* in mock'
res=''
for word in var.split():
    res+=word[::-1]+' '
print(res)

var='get p* in mock'
res=''
for word in var.split():
    res=word+' '+res
print(res)
print(' '.join(var.split()[::-1]))

var='get p* in mock'
print(var[:len(var)//2])

var='get p* in mock'
print(var[len(var)//2:])

s=input('enter a string:')
res=''
for i in range(len(s)):
    if i%2==0:
        res+=s[i]
print(res)

s='hello'
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        print(s[sv:ev])

s='hello'
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        if(s[sv:ev]==s[sv:ev][::-1]):
            print(s[sv:ev])

s='hello'
for ch in s:
    if ch.isalpha() and ch not in 'aeiouAEIOU':
        print(ch)
for ch in s:
    if ('A'<=ch<='Z' or 'a'<=ch<='z') and ch not in 'aeiouAEIOU':
        print(ch)

s='wE wiLL learn All skills 100%'
spec,vow,con,dig,upp,low=0,0,0,0,0,0
for ch in s:
    if ('A'<=ch<='Z' or 'a'<=ch<='z'):
        if ('A'<=ch<='Z' or 'a'<=ch<='z') and ch not in 'aeiouAEIOU':
            con+=1
        if ('A'<=ch<='Z' or 'a'<=ch<='z') and ch  in 'aeiouAEIOU':
            vow+=1
        if 'A'<=ch<='Z':
            upp+=1
        if 'a'<=ch<='z':
            low+=1
    elif ch in '1234567890':
        dig+=1
    else:
        spec+=1
print(spec,vow,con,dig,upp,low)

s='wE wiLL learn All skills 100%'
print([ch[0] for ch in s.split()])

s='wE wiLL learn All skills 100%'
print([(word,len(word)) for word in s.split()])

print([val*val for val in range(10,21)])

print([val for val in range(10,21)if val%2==0])

names=['lara','steve','bob','scott','alex','abi','ajith']
print([name for name in names if name[0] in 'aeiouAEIOU'])

languages=('python','java','mern','html','php','perl')
print([lang for lang in languages if lang[0]=='p'])

languages=('python','java','mern','html','php','perl')
print([lang for lang in languages if len(lang)<6])

languages=('python','java','mern','css','html','php','perl')
print([lang[::-1] if len(lang)%2!=0 else lang for lang in languages])
'''


n=8
for num in range(1,n+1):
    print(num,end='')








            
            
