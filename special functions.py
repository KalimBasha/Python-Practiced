'''n=5
print('\n'.join(list(map(lambda n:'* '*n,range(n,0,-1)))))
num=5
print('\n'.join(list(map(lambda m,n:' '*m+'* '*n,range(0,num),range(num,0,-1)))))
num=5
print('\n'.join(list(map(lambda m,n:'  '*m+'* '*n,range(num-1,-1,-1),range(1,num*2,2)))))
num=5
print('\n'.join(list(map(lambda sp,st:'  '*sp+'* '*st,range(num-1,-1,-1),range(1,num+1)))))
num=5
print('\n'.join(list(map(lambda sp,st:'  '*sp+'* '*st,range(0,num),range(num,0,-1)))))
num=5
print('\n'.join(list(map(lambda st:'* '*st,range(num,0,-1)))))
num=5
print('\n'.join(list(map(lambda sp,st:'  '*sp+'* '*st,range(num-1,-1,-1),range(1,num+1)))))
num=5
print('\n'.join(list(map(lambda sp,val:' '*sp+(str(val)+ ' ')*val,range(num-1,-1,-1),range(1,num+1)))))
def even(num):
    if num%2==0:
        return True
print(list(filter(even,range(1,30))))
def arm(num,res=0):
    dup,pow=num,len(str(num))
    while num!=0:
        rem=num%10
        res+=rem**pow
        num//=10
    return res==dup
print(list(filter(arm,range(1,30))))
num=12345
def rev(num,p=10**(len(str(num))-1)):
	if num==0:
		return 0
	return (num%10)*p+rev(num//10,p//10)
print(rev(num))'''
