r=range(3)

#range迭代器独立分开
l1=iter(r)
print(next(l1))
print(next(l1))

l2=iter(r)
print(next(l2))
print(next(l2))


#zip共享迭代器
z=zip([1,2,3],[4,5,6])
for x in z:
    print(x)
