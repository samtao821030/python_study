choice='ham'
value={'sam':9,'tom':10,'ham':12}[choice]
print(value)

branch={'spam':1.25,
        'ham':1.99,
        'eggs':0.99
        }
print(branch.get('spam','Bad choice!'))

print(branch.get('xx','Bad choice!'))

def default():
    print('我是默认的!')

branch.get('xx',default)()

a='t' if 'spam' else 'f'
print(a)
a='t' if '' else 'bb'
print(a)