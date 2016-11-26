f=open('data.txt','w')
f.write('hello\n')
f.write('world\n')
f.close()
f=open('data.txt')
# text=f.read()
# print(text)
for line in open('data.txt'):
    print(line)