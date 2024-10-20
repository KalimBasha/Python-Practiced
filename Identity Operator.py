a='Kalim Basha'
b='KalimBasha'
c='kalim basha'
z='kalim basha'
d=10
e=10
k=('hii','hello',['a'])
l=['hii','hello']
m=('hii','hello',['a'])
n=['hii','hello']
print (a is b)
print (a is c)
print(c is z)# True bcz strings are immutable
print (d is e)
print (k is m)#False bcz tuples are immutable but it contains mutable elements
print (l is n)#false bcz lists are mutable.Muable elements returs the o/p as false
print (l is not n)
print (d is not e)
