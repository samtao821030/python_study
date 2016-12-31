a=[1,2,3]
for i in a:
    print(i,end=' ')

print()

b=iter(a)
while True:
    try:
        x=next(b)
    except StopIteration:
        break;
    print(x,end=' ')

