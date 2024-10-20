'''
sentence='hello world welcome to python programming hi there'
var=sentence.split()
d1={}
for word in var:
    if word[0] not in d1:
        d1[word[0]]=[word]
    else:
        d1[word[0]]+=[word]
print(d1)

d={'a':'hello','b':100,'c':10.9,'d':'world'}
d1={}
for val in d.items():
    if type(val[1])==str:
        d1[val[0]]=val[1][::-1]
    else:
        d1[val[0]]=val[1]
print(d1)

#count using inbuilt method
st=input('Enter a string:')
d1={}
for ch in st:
    if ch not in d1:
        d1[ch]=[st.count(ch)]
print(d1)

#count using without inbuilt method
st=input('Enter a string:')
d1={}
for ch in st:
    if ch not in d1:
        d1[ch]=1
    else:
        d1[ch]+=1
print(d1)

num=(1,2,3,4,5,6,7,8,9,10)
d={0:[],1:[]}
for n in num:
    if n%2==0:
        d[0]+=[n]
    else:
        d[1]+=[n]
print(d)

var=input('Enter a string:')
d={}
for ch in var:
    if ch not in d and var.count(ch)>1:
        d[ch]=[var.count(ch)]
print(d)

items=['lotus-flower','lilly-flower','cat-animal','sunflower-flower','dog-animal']
d={}
for ele in items:
        if ele.endswith('flower'):
            res=ele.split('-')
            if 'flower' not in d:
                d['flower']=[res[0]]
            else:
                d['flower']+=[res[0]]
        else:
            res=ele.split('-')
            if 'animal' not in d:
                d['animal']=[res[0]]
            else:
                d['animal']+=[res[0]]            
print(d)

items=['lotus-flower','lilly-flower','cat-animal','sunflower-flower','dog-animal']
d={}
for ele in items:
    res=ele.split('-')
    if res[1]=='flower':
        if 'flower' not in d:
            d['flower']=[res[0]]
        else:
            d['flower']+=[res[0]]
    else:
        if 'animal' not in d:
            d['animal']=[res[0]]
        else:
            d['animal']+=[res[0]]
print(d)       

files=('apple.txt','yahoo.pdf','gmail.pdf','amazon.pdf','google.txt','facebook.pdf','flipkart.pdf')
d={}
for ele in files:
        res=ele.split('.')
        if res[1]=='txt':
                if res[1] not in d:
                        d[res[1]]=(res[0],)
                else:
                        d[res[1]]+=(res[0],)
        else:
                if res[1] not in d:
                        d[res[1]]=(res[0],)
                else:
                        d[res[1]]+=(res[0],)
print(d)

apps=['apple','google','apple','yahoo','google','yahoo','gmail','gmail','amazon','apple']
d={}
for i in enumerate(apps):
        if i[1] not in d:
                d[i[1]]=[i[0]]
        else:
                d[i[1]]+=[i[0]]
print(d)
for i,app in enumerate(apps):
        print(i,app)
'''
d={'a':1,'b':3,'c':4.5,'d':False}
d1={}
for ele in d.items():
        d1[ele[1]]=ele[0]
print(d1)

















