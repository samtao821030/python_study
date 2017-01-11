def gensquare(N):
    for i in range(5):
        yield i**2;

for i in gensquare(5):
    print(i,end=",")
print()

def gen():
    for i in range(10):
        x=yield i+1
        print(x)

g=gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

next(g)
next(g)
next(g)
