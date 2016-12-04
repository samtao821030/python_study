from __future__ import division
print(4e210)
print(1!=5)
a=int(3.45)
print(a)
b=float(1)
print(b)

a=4
#逗号相隔的表达式会组成元组
b=a*2,a/2
print(b)

a=repr('spam')
b=str('spam')
print(a)
print(b)

x=2
y=4
z=6
print(x<y<z)

print(10//4)


print(10/4)

a=5//2, 5//-2.0
print(a)

print(oct(64))
print(hex(64))
print(bin(64))

print(eval('64'))
print(eval('0o100'))
print(eval('0x40'))
print(eval('0b1000000'))

print('{0:o},{1:x},{2:b}'.format(64,64,64))