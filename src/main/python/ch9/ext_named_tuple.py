from collections import namedtuple

record=namedtuple('record',['name','age','jobs'])
new_record=record(name='taosm',age=34,jobs=['developer','manager'])
print(new_record)

dict=new_record._asdict()
print(dict)