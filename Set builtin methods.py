
a={'kalim','susmii',53,64,89,(8,90),53}
print(a.add(64))
print(a)
print(a.add(9.01))
print(a)

print(a.update('hello'))
print(a)
print(a.update([12,23]))
print(a)
#print(a.update([12,[23,45]]))
#print(a.update(1223))
print(a.update({'a':'kalim','b':23}))
print(a)

print(a.remove('kalim'))
print(a)
#print(a.remove(4))

#print(a.discard())
print(a.discard(90))
print(a)
print(a.discard(9.01))
print(a)

print(a.pop())
print(a)
print(a.pop())
print(a)

print(a.clear())
print(a)

b={1,2,3,4,5}
c={3,7,9,0,2}
print(b.union(c))

print(b.intersection(c))
print(c.intersection(b))

print(b.difference(c))
print(c.difference(b))
