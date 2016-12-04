s1="""
david is a %d year %s
"""
print(s1%(10,'boy'))

s2="""
david is a %(year) year %(gender)
"""

reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""

values = {'name': 'Bob', 'age': 40}
print(reply % values)

template='{0},{1},{2}'
print(template.format('tao','shang','ming'))

template='{moto},{bank},{name}'
print(template.format(moto='car',bank='guangda',name='shangming'))

print('{0:10}={1:>10}'.format('dex','harry'))