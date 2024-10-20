'''def ldistance(str1,str2=''):
    l=[]
    for ch in str1:
        if ch not in str2:
            str2+=ch
        else:
            print(str2[str2.index(ch):len(str2)])
            str2+=ch
    
print(ldistance('madam'))'''

def decorat(args):
    def inner(l):
        l2=[]
        i=0
        def values(i):
            try:
                for val in l:
                    l2.append(int(val))
                    
                
            except ValueError as msg:
                def value(
            print(i)
        print(l2)
        return args(l2)
        
            
    return inner
@decorat
def maximum(l):
    maxval=l[0]
    for i in range(len(l)):
        if l[i]>maxval:
            maxval=l[i]
    return maxval
print(maximum([20,50,'susmi','20','kalim',40,90]))
'''l=[20,50,'susmi','20','kalim',40]
l2=[]
            
try:
    for val in l:
        l2.append(int(val))
    print(l2)
finally:
    print('hi')'''
