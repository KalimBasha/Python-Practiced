
#And
a=20
b=67
print(a>b and a==b)
print(a<b and a>b)
print(a>b and k>b)
#print(a<b and k>b)
print([0] and 0)
print({} and '')
print(0 and 0.0 )

#Or
a=30
b=100
print(a<b or k>b)
#print(a>b or k>b)
print(a>b or a<b)
print(a>b or a==b)
print(0 or 1)
print(0 or 0.0)
print(8 or 0)

#Not
print(not False)
print((not False) or (not True) or True)
