'''
#linear search
L=[12,-3,1,-20,5]
t=5
for ind in range(len(L)):
    if t==L[ind]:
        print(f'Index position of value {t} is {ind}')
        break
else:
    print(-1)'''
'''
#binary search
L=[-20,-3,0,1,5]
t=80

low=0
high=len(L)-1
while low<=high:
    mid=(low+high)//2
    if t<L[mid]:
        high=mid-1
    elif t>L[mid]:
        low=mid+1
    else:
        print(mid)
        break
else:
    print(-1)'''
'''
#interpolation search
L=[-20,-3,0,1,5]
t=1

low=0
high=len(L)-1
while low<=high and L[low]<=t<=L[high]:
    mid=int(low+((high-low)/(L[high]-L[low])*(t-L[low])))
    if t<L[mid]:
        high=mid-1
    elif t>L[mid]:
        low=mid+1
    else:
        print(mid)
        break
else:
    print(-1)'''
'''
#bubble sort
L=[420,87,1,99,-28,1]
for ind1 in range(len(L)-1,-1,-1):
    for ind2 in range(ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L)'''
'''
#selection sort
L=[420,87,1,99,-28,1]
for ind1 in range(len(L)-1):
    i=ind1
    for ind2 in range(ind1+1,len(L)):
        if L[i]>L[ind2]:
            i=ind2
    L[ind1],L[i]=L[i],L[ind1]
print(L)'''
'''
#quick sort
L=[420,87,1,99,87,-28,1]
def quick(L):
    if len(L)<=1:
        return L
    pivot=L[-1]
    left=[val for val in L[:len(L)-1] if val<pivot]
    right=[val for val in L[:len(L)-1] if val>=pivot]
    return quick(left)+[pivot]+quick(right)
print(quick(L))'''
'''
#merge sort
def conquer(L,left,right):
    lind,rind,mind=0,0,0
    while lind<len(left) and rind<len(right):
        if left[lind]>right[rind]:
            L[mind]=right[rind]
            rind+=1
        else:
            L[mind]=left[lind]
            lind+=1
        mind+=1
    while lind<len(left):
        L[mind]=left[lind]
        lind+=1
        mind+=1
    while rind<len(right):
        L[mind]=right[rind]
        rind+=1
        mind+=1
def divide(L):
    if len(L)>1:
        mid=len(L)//2
        left=L[:mid]
        right=L[mid:]
        divide(left)
        divide(right)
        conquer(L,left,right)
L=[420,87,1,99,87,-28,1]
divide(L)
print(L)'''
'''
l=['a',10,30,'kl',98]
for i in range(len(l)):
    if i%2==0:
        print(l[i])'''
'''
d={'a':10,'b':40,'c':45}
d2={'a':20,'b':30,'c':15}
d1={}
for i in d.items():
    if i[0] not in d1:
        d1[i[0]]=[i[1]]
    else:
        d1[i[0]]+=[i[1]]
for i in d2.items():
    if i[0] not in d1:
        d1[i[0]]=[i[1]]
    else:
        d1[i[0]]+=[i[1]]
print(d1)'''
'''
def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
            break
    return True
def palindrome(num):
    dup=num
    res=0
    while num != 0:
        rem = num%10
        res = res*10+rem
        num//=10
    return dup==res
print('palyprime' if prime(12) and palindrome(12) else 'not')'''
'''
num=20
spaces=num-1
for i in range(1,num*2,2):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(i):
        if(i==1 or i==num*2-1):
            print('*',end='')
        elif(st==0 or st==i-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
    spaces-=1
'''
'''
s='python'
spaces=len(s)-1
for i in range(-1,-len(s)-1,-1):
    for sp in range(spaces):
        print(' ',end='')
    for ch in range(-1,i-1,-1):
        print(s[ch],end='')
    print()
    spaces-=1
'''
a=0
b=0
nums=[2,7,11,15]
target=
for ind1 in range(len(nums)):
    a=ind1
    for ind2 in range(len(nums)):
        if a!=ind2:
            b=nums[a]+nums[ind2]
            if b==target:
                print(a,ind2)
                break
    




















