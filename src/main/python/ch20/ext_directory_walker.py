import os
p=os.walk("c:/")
for (root,subs,files) in p:
    for name in files:
        if name.endswith('txt'):
            print(root,name)