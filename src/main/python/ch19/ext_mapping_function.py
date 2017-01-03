counters=[1,2,3,4,5,6]

def inc(x):return x+10

print(list(map(inc,counters)))

print(list(map((lambda x:x+10),counters)))