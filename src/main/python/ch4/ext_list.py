l = [123,'taosm',1.2]
print(l[:1])
l=l+[456,'spam']
print(l)
l.pop(1)
print(l)
m=['bb','aa','cc']
m.sort()
print(m)
m.reverse()
print(m)
n=[[1,2,3],
   [4,5,6],
   [7,8,9]
   ]
print(n[1])
print(n[1][2])
col2=[row[1] for row in n]
print(col2)
col3=[row[1]+1 for row in n]
print(col3)
doubles=[ c*2 for c in 'spam']
print(doubles)
o=[row for row in n]
print(o)
p=[sum(row) for row in n]
print(p)
q=(row for row in n)
print(next(q))
print(next(q))
print(next(q))
help(ord('x'))