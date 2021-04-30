
import json

# function to add to JSON
def write_json(data, filename='data.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

json_file = open('data.json')

json_data = json.load(json_file)


# get names from the txt file using file handler

names = [name.strip('\n') for name in open('name.txt','r')]
not_exist_names = names.copy()


def isNameExist(data,names):
    for n in names:
        for ind,d in enumerate(data):
            if n == d['name']:
                try:
                    not_exist_names.remove(d['name'])
                except ValueError:
                    print("ValueError")
    return not_exist_names

def create(data):
    id = len(json_data)
    for nen in data:
        #print(nen)
        id = id + 1
        not_existing_names_data = {"id": id, "name": nen}
        #print(not_existing_names_data)
        json_data.append(not_existing_names_data)
    return json_data
                
    

name_not_found = isNameExist(json_data,names)
data = create(name_not_found)
write_json(data)




