
import json

# function to add to JSON
def write_json(data, filename='data.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

json_file = open('data.json')

json_data = json.load(json_file)

#print(json_data)

# get names from the txt file using file handler

names = [name.strip('\n') for name in open('name.txt','r')]


def isNameExist(data,names):
    for n in names:
        for ind,d in enumerate(data):
            if n == d['name']:
                try:
                    names.remove(d['name'])
                except: 
                    print(ind,d['name'])
                    id = len(json_data) + 1
                    json_data.append({"id": id, "name": d['name']})
            #else:
                #print(str(ind)+d["name"].center(50,"."))
                
    

isNameExist(json_data,names)

print(json_data)
