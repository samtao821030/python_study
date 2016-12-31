def maker(n):
    def action(x):
        print(x**n)
    return action

f=maker(2)
f(3)