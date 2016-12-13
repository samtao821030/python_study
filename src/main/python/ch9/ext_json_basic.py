person=dict(name='taosm',age=34,salary=5000)
person_score=dict(person=person,score=80)
import json
json_str=json.dumps(person_score)
print(json_str)
json_obj=json.loads(json_str)