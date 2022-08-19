
# dict

person = {"name":"Ali", "languages":["Python","C#"]}

result = person["name"]
result = person["languages"]
result = person["languages"][0]

print(result)

import json

person_string = '{"name":"Ali", "languages":["Python","C#"]}'

# JSON string to Dict

# result1= json.loads(person_string)

# with open("person.json") as f:
#     data = json.load(f)
#     print(data)
#     print(data['name'])

# print(type(result1))
# print(result1)

person_dict = {
    "name" : "Ali",
    "languages": ["Python", "C#"]
}

# result2 = json.dumps(person_dict)
# print(result2)

# with open("person.json","w") as f:
#     json.dump(person_dict,f)


person_dict = json.loads(person_string)

result3 = json.dumps(person_dict, indent = 4, sort_keys= True)

print(person_dict)
print(result3)
