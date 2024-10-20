
import keyword
print(keyword.kwlist)

#Integer
a=10
print(type(a))
print(id(a))
b=0
print(type(b))

#Float
c=2.0
print(type(c))

#Boolean
print(bool())
var=True
print(type(var))
print(var+False)

#Complex
k=8+3j
print(type(k))
l=0j
print(type(l))

#String
str='kalim'
print(type(str))
print(str[2])
str[2]='h'
print(str)
r='kalim is no 1'
print(r)
print(r[-4])

#Lists
lt=[0,'kalim',[1,'hero'],3,2.0]
print(lt)
print(lt[4])
print(lt[-3][-2])
lt[1]='hii'
print(lt)

# Tuples
tp=(1,0.0,'Butter',[2,8,'csk'],False)
print(tp)
print(tp[2])
print(tp[-2])
#tp[2]='Park'
print(tp)
print(tuple())
he=(8)
print(type(he))
ha=(3,)
print(type(ha))

#Set
print(set())
#hi={'kalim',2,5.8,[0,2,1],True,(7,'hlo')}
hai={'kalim',2,5.8,True,(7,'hlo')}
print(hai)
#print(hai[3])
hai.add('basha')
print(hai)
hai.add(2)
print(hai)
hey={2,2,2,2}
print(len(hey))

#Dict
print(dict())
dt={'a':'kalim','age':21,'gender':'male'}
print(dt)
dt={'a':'kalim','age':21,'gender':'male','a':'basha','height':[21,24]}
print(dt)
#print(dt[1])
print(dt['age'])
dt['b']='kalim'
print(dt)



