d={'food':'spam','quantity':4,'color':'pink'}
print(d['food'])
print(d['color'])
d['age']=40
print(d)
bob1=dict(name='bob',job='dev',age=40)
bob2=dict(zip(['name','job','age'],['bob','dev',40]))
print(bob2)
rec={
        'name':{'first':'bob','last':'smith'},
        'jobs':['dev','mgr'],
        'age':40.5
     }
rec['jobs'].append('mac');
rec['name']['second']='my_second'
print(rec)
f={'a':1,'c':3,'b':2}
if  not 'e' in f:
    print('missing')
value=f.get('e',0)
value1=f['x'] if 'x' in f else 0
print(value1)

ks=list(f.keys())
ks.sort()
for key in ks:
    print(key,'=>',f[key])

for c in 'spam':
    print(c.upper())

x=4
while x>0:
    print('spam!'*x)
    x-=1