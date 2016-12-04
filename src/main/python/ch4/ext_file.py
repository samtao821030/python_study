f=open('data.txt','w');
f.write('nimei\nok\nok')
f.close()
f=open('data.txt')
text=f.read()
print(text)
print(text.split())
for line in open('data.txt'):
    print(line)