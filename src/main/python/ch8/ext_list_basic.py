a=[1,2,3]+[4,5,6]
print(a)
for x in [1,2,3]:
    print(x,end=' ')
print()
res=[c*4 for c in 'SPAM']
print(res)

l=list(map(abs,[-1,-2,3,1,10,9]))
print(l)

l=['spam','harry','benz']
l[0]='eggs'
l[1:3]=['good','night']
print(l)

l=[1,2,3]
l[1:2]=[4,5]
print(l)
l[1:1]=[6,7]
print(l)

l=[1]
l[:0]=[2,3,4]
print(l)

l[len(l):]=[6,7,8]
print(l)

a=['eat','more','spam']
a.append('please')
a.sort()
print(a)

b=[1,2,3,4]
print(list(reversed(b)))

c=[]
c.append(1)
c.append(2)
print(c)

d=['spam', 'eggs', 'ham']
d.insert(1,'banana')
print(d)
d.pop(1)
print(d)