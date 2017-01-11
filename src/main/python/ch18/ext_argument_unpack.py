def func1(a,b,c,d):
    print(a,b,c,d)

param1=(1,2,3,4)
func1(*param1)

param2=dict(a=1,b=2,c=3,d=4)
func1(**param2)
