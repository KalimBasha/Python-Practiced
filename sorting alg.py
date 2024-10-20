'''
#bubble sort
L=[98,760,0,34,23,2]
for ind1 in range(len(L)-1,0,-1):
    for ind2 in range(ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L)
'''

'''
#selection sort
L=[20,-34,-7,0,2,56]
for ind1 in range(len(L)-1):
    li=ind1
    for ind2 in range(ind1+1,len(L)):
        if L[li]>L[ind2]:
            li=ind2
    L[ind1],L[li]=L[li],L[ind1]
print(L)
'''

'''
#quick sort
def quick(L):
    if len(L)<=1:
        return L
    pivot=L[0]
    left=[val for val in L[1: ] if val<pivot]
    right=[val for val in L[1: ] if val>=pivot]
    return quick(left)+[pivot]+quick(right)
L=[420,87,0,-12,-45,7,10]
print(quick(L))
'''
'''
def quick(L):
    if len(L)<=1:
        return L
    pivot=L[0]
    left=[]
    right=[]
    for ind in range(1,len(L)):
        if pivot>L[ind]:
            left.append(L[ind])
        else:
            right.append(L[ind])
    return quick(left)+[pivot]+quick(right)
L=[420,87,0,-12,-45,7,10]
print(quick(L))
'''
'''
#by pranay sir
def quick(L):
    if len(L)<1:
        return L
    pivot=L[len(L)//2]
    left = []
    right = []
    for ind in range(len(L)):
        if L[ind] > pivot:
            right.append(L[ind])
        elif L[ind] == pivot:
            right.append(L[ind])
        else:
            left.append(L[ind])
    print(left,pivot,right)
    return quick(left)+[pivot]+quick(right)
L=[20,2,-3,-87,420,2,7,1020]
print(quick(L))
'''

def quick(L):
    if len(L)<=1:
        return L
    pivot=L[len(L)//2]
    left=[val for val in L[:] if pivot>val]
    right=[val for val in L[:] if pivot<=val]
    return quick(left)+[pivot]+quick(right)
L=[-2,-10,36,-2,420,8]
print(quick(L))

'''
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
        print(L)
def divide(L):
    if len(L)>1:
        mid=len(L)//2
        left=L[:mid]
        right=L[mid:]
        divide(left)
        divide(right)
        print(L,left,right)
        conquer(L,left,right)
L=[8,10,-2,6,4]
divide(L)
print(L)
'''












