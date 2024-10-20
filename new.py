'''l=[20,3,-1,0,43,12]
for ind1 in range(len(l)):
    for ind2 in range(ind1+1,len(l)):
        if l[ind1]<l[ind2]:
            l[ind1],l[ind2]=l[ind2],l[ind1]
print(l)
            
n=[val for val in range(2)]
for ind1 in range(len(arr)):
    for ind2 in range(ind1+1,len(arr)):
        if arr[ind1]<arr[ind2]:
            arr[ind1],arr[ind2]=arr[ind2],arr[ind1]
print(arr[1])

arr = list(map(int, input().split()))
arr1=set(arr)
print(arr1)
for ind1 in range(len(arr1)):
    for ind2 in range(ind1+1,len(arr1)):
        if arr1[ind1]<arr1[ind2]:
            arr1[ind1],arr1[ind2]=arr1[ind2],arr1[ind1]
print(arr1[1])

students=[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name,score))
for student in students:
       arr = sorted(student[1])
       print(arr)'''

'''
#int to binary
num=int(input('number:'))
res=0
power=1
while num!=0:
    rem=num%2
    res+=rem*power
    num//=2
    power*=10
print(res)

#binary to int
num=int(input('number:'))
res=0
pos=1
while num!=0:
    rem=num%10
    res+=rem*pos
    num//=10
    pos*=2
print(res)
'''

num=int(input('num:'))
a=len(str(num))
sq=num*num
print(sq)
i=0
res=''
while i!=a:
    rem=sq%10
    res=str(rem)+res
    i+=1
    sq//=10
    print(res)
if num==int(res):
    print('automorphic')
else:
    print('not')
    
