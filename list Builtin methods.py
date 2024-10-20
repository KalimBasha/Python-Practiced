

a=['kalim',7,6]
print(a.append([23,7]))
print(a)

print(a.insert(1,230))
print(a)
print(a.insert(1,('hii',23)))
print(a)
print(a.insert(-2,800))
print(a)
print(a.insert(-1,230))
print(a)

a=['kalim',7,6]
print(a.extend([12,'kalim']))
print(a)
print(a.extend('!@#$%[]'))
print(a)

#print(a.remove('hii'))
print(a)

print(a.pop())
print(a)
print(a.pop(3))
print(a)
#print(a.pop(18))

print(a.clear())
print(a)

b=['k','a','l','i','m',1,2,365,2,(87,'hii'),1,{65,'hello'}]
print(b.index(2))
print(b.index(2,7))
print(b.index(2,3,7))

s=b.copy()
print(s)
print(b is s)

#print(b.count())
print(b.count(1))
#print(b.count(1,6))

c = ['kalim','basha']
print('is'.join(c))
print('-'.join(c))

print(c.reverse())
print(c)

d=[1,2,365,2]
print(d.sort())
print(d)
print(d.sort(reverse=True))
print(d)

#In built Methods for Tuple
l=('kalim',23,'susmii',22,'guntur',23)
print(l.count(23))
print(round(23.786,1))
print(l.index('susmii'))
#print(l.rindex(22))
print(l.index(23,2))




