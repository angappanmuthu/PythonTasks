
import json 

json_file = open('data.json')

json_data = json.load(json_file)

for i in json_data:
    print(i)

def get_each_name():
    return ''
