import json
dump = {}


#name:[list of votes]
votes = {}
for i in range(126):
    f = open("data_clean/"+str(i)+"_clean.json")
    data_rough = f.read()
    data = json.loads(data_rough)
    for mp in data.keys():
	if not (mp in votes.keys()):
		votes[mp]= data[mp]
	else:
		votes[mp] = {"yea" : votes[mp]["yea"] + data[mp]["yea"], "nay": votes[mp]["nay"] + data[mp]["nay"], "paired" : votes[mp]["paired"] + data[mp]["paired"]}
	
fdmp = open("data_clean/result_clean.json","w")  
fdmp.write(json.dumps(votes))
