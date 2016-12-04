myjob='hacker'
for c in myjob:print(c,end=',')
print('k' in myjob)
print(myjob[:-1])
print(myjob[1:])

s='abcdefghijklmn'
print(s[::2])
print(s[::-1])
s='abcdefg'
print(s[5:1:-1])

print(int("42"))
print(str(42))

print(str('spam'),repr('spam'))

print(ord('s'))
print(chr(115))

print(int('1101',2))
print(str(bin(13)))

print('this is %d %s bird'%(1,'dead'))