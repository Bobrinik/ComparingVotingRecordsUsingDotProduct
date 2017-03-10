import json
dump = {}


#name:[list of votes]
for i in range(126):
    f = open("data/"+str(55+i)+".json")
    data_rough = f.read()
    data = json.loads(data_rough)
    for vote in data['votes']:
        if vote['name'] in dump.keys():
            dump[vote['name']].append(vote['votes'])
        else:
            dump[vote['name']] = []

fdmp = open("data/data.json","w")  
fdmp.write(json.dumps(dump))  
