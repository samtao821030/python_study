d=(1,2,3,4)
f=open('datafile.pkl','wb')
import pickle
pickle.dump(d,f)
f.close()

f=open('datafile.pkl','rb')
new_d=pickle.load(f)
print(new_d)