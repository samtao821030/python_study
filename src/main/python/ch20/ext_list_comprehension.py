res1=list(map(ord,'spam'))
print('res1:'+str(res1))

res2=[ord(x) for x in 'spam']
print('res2:'+str(res2))

res= [x+y for x in [0,1,2] for y in [3,4,5]]
print(list(res))