'''
#merge 2 lists
l1=(input('enter:')).split(',')
l2=(input('enter:')).split(',')
print(l1+l2)

#print all numbers
l=['abc','123','hello','23']
l1=[]
for ch in l:
    if ch.isdigit():
        l1+=ch
print(l1)

#alternative characters
var='hello world'
res=[]
for i in range(len(var)):
    if i%2==0:
        res+=var[i]
print(res)

#even no of characters
l=['apple','instagram','whatsapp','amazon','facebook','snapchat','google']
res=[]
for i in range(len(l)):
    if len(l[i])%2==0:
        res.append(l[i])
print(res)

#reverse a list
l=['hi','hello','python','bye']
res=l[::-1]
l1=[]
for ch in range(len(res)):
    var=res[ch][::-1]
    l1.append(var)
print(l1)

#odd num
num=int(input("Enter Number:"))
l=[]
for n in range(1,num+1):
    if n%2!=0:
        l.append(n)
print(l)

#duplicates
name=['apple','google','yahoo','google','apple','amazon','google']
l=[]
for ele in name:
    if name.count(ele)>1:
        l.append(ele)
print(l)

#find greatest
num=[24,13,45,27,65]
#with method
num.sort(reverse=True)
print(num[0])
#without method
max=0
for n in num:
    if max<n:
        max=n
print(max)

#sort a list
a=[3,4,1,7,2,12,8,6,9,11]
a1=[]
a2=[]
for num in a:
    if num%2!=0:
        a1.append(num)
        a1.sort()
    else:
        a2.append(num)
        a2.sort()
print(a1+a2)

sentence='hello123 world567 welcome to 9724python'
res=0
for ch in sentence:
    if ch.isdigit() and int(ch)%2==0:
        res+=int(ch)
print(res)

#duplicates
name=['apple','google','yahoo','google','apple','amazon','google']
l=[]
for ele in name:
    if ele not in l:
        l.append(ele)
print(l)
'''
