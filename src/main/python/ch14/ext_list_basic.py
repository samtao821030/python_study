l=[1,2,3,4,5,6]
a=[i*2 for i in l]
print(a)

lines=[line.rstrip() for line in open('ext_iterator_advance.py')]
print(lines)

lines=[line.rstrip() for line in open('ext_iterator_advance.py') if line[0]=='p']
print(lines)