import json
dump = {}


#name:[list of votes]
for i in range(126):
    f = open("data/"+str(55+i)+".json")
    data_rough = f.read()
    data = json.loads(data_rough)
    for vote in data['votes']:
        dump[vote['name']] = vote['votes']
        fdmp = open("data_clean/"+str(i)+"_clean.json","w")  
        fdmp.write(json.dumps(dump))
