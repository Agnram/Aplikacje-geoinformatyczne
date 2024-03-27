import json

with open('teksty.json') as json_file:
    data = json.load(json_file)




print(dir(data["teksty"]))