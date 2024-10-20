'''
row=int(input("Enter no of rows:"))
col=int(input("Enter no of columns:"))
mat=[]
for r in range(row):
    line=[]
    for c in range(col):
        line.append(int(input("Enter a value:")))
    mat.append(line)
print(mat)
'''
'''
row=int(input("Enter no of rows:"))
col=int(input("Enter no of columns:"))
print([[int(input("Enter a val:")) for c in range(col)] for r in range(row)])
'''
'''
m1=[[2,3],[3,4]]
m2=[[2,3],[3,4]]
if len(m2)==len(m1):
    for r in range(len(m1)):
        for c in range(len(m2[0])):
            m1[r][c]=m1[r][c]+m2[r][c]
    print(m1)
else:
    print('Not possible')
'''

m1=[[2,3],[3,4],[4,5]]
m2=[[2,3,4],[3,4,5]]
if len(m1[0])==len(m2):
    m=[]
    for r in range(len(m1)):
        line=[]
        for c in range(len(m1[0])):
            res=0
            for v in range(len(m2)):
                res+=m1[r][v]*m2[v][c]
            line.append(res)
        m.append(line)
    print(m)
