counters=[1,2,3,4,5,6]

def inc(x):return x+10

print(list(map(inc,counters)))

print(list(map((lambda x:x+10),counters)))

list1=[x for x in range(5) if x%2==0]
print(list1)

e=filter((lambda x:x%2==0),range(5))

for x in e:
    print(x)