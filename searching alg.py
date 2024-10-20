'''
#linear
L=[2,0,-3,4,99,87,76]
target=99
for ind in range(len(L)):
    if L[ind]==target:
        print(ind)
        break
else:
    print(-1)
#using func
def linear(L,target):
    for ind in range(len(L)):
        if L[ind]==target:
            return ind
    return -1
L=[2,0,-3,4,99,87,76]
target=99
print(linear(L,target))
'''
'''
#binary
L=[2,0,-3,4,99,87,76]
L.sort()
print(L)
target=99
low=0
high=len(L)-1
while low<=high:
    mid=(low+high)//2
    if L[mid]<target:
        low=mid+1
    elif L[mid]>target:
        high=mid-1
    elif L[mid]==target:
        print(mid)
        break
else:
    print(-1)

#using func
def binary(L,target,low,high):
    while low<=high:
        mid=(low+high)//2
        if L[mid]<target:
            low=mid+1
        elif L[mid]>target:
            high=mid-1
        elif L[mid]==target:
            return mid
    return -1
L=[-3, 0, 2, 4, 76, 87, 99]
target=87
print(binary(L,target,0,len(L)-1))
'''
'''
#interposition
L=[-3, 0, 2, 4, 76, 87, 99]
target=76
low=0
high=len(L)-1
while low<=high and L[low]<=target<=L[high]:
    mid=int(low+(high-low)/(L[high]-L[low])*(target-L[low]))
    if L[mid]<target:
        low=mid+1
    elif L[mid]>target:
        high=mid-1
    elif L[mid]==target:
        print(mid)
        break
else:
    print(-1)
'''
