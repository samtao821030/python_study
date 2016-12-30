L=[0,1,2]
def change(list):
    list[0]='spam'

change(L[:])
print(L)
change(L)
print(L)

def multiple(x,y):
    return x,y
t=multiple(1,2)
print(t)

