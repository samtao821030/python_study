print((1,2)+(3,4))
x=(40)
print(x)

t1=('c','a','d','b')
list(t1).sort()
tmp=list(t1)
tmp.sort()
t1=tuple(tmp)
print(t1)

t2=('c','a','d','b')
print(sorted(t2))

l=[x*2 for x in t2]
print(l)