'''
a={'a':'kalim','b':21,(21,):23}
print(type(a))
#print(a.pop())
#print(a.pop(23))
print(a.pop('b'))
print(a)

#print(a.popitem('a'))
print(a.popitem())
print(a)

print(a.clear())
print(a)

a={(23,):21,'k':23}
print(a)
a['m']=34
print(a)

var=((23,24),(98,97))
a.update(var)
print(a)

print(a.popitem())
print(a)
print(a.pop('rr'))'''

d={}
d['kalim']='coffee'
print(d)
d.update(('56',))
print(d)


