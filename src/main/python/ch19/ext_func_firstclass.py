def echo(name):
    print(name+" is a good guy")

x= echo
x('taosm')

def indirectCall(func,name):
    func(name)

indirectCall(echo,'bokai')

print(echo.__code__.co_argcount)