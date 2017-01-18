class c1:
    pass

class c2:
    pass

class c3(c1,c2):
    def setname(self,name):
        self.name=name

l1=c3()
l2=c3()

l1.setname('tao')
l2.setname('haha')

print(l1.name)

