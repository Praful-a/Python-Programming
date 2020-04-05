'''JavaScript Object Notation'''
import json
import os
os.chdir('/Users/praful/desktop/python/JSON/')

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
data = json.loads(people_string)

# print(type(data))
# print(type(data['people']))

for person in data['people']:
    # print(person)
    # print(person['name'])
    del person['phone']
new_string = json.dumps(data, indent=2)
# new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state)
    print(state['name'], state['abbreviation'])
    del state['area_codes']

with open('new_state.json', 'w') as f:
    json.dump(data, f, indent=2)
