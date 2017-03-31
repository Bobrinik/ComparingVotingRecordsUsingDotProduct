import json
from matplotlib import pyplot as plt

def dot_product(vote1, vote2):
    keys = ['nay','paired','yea']
    result = [vote1[key]*vote2[key] for key in keys]
    sum = 0
    for e in result:
        sum = sum + e
    return sum

def policy_compare(mp_1, mp_2, votes):
    vote1 = votes[mp_1]
    vote2 = votes[mp_2] 
    return dot_product(vote1, vote2)

#return name of the member of parlament that has the highest likelyhood measured by dot product
def most_simillar(mp,votes):
    similarity = {}
    for member in votes.keys():
        if(not member == mp):
            similarity[member] = policy_compare(mp, member, votes)
    max = similarity[similarity.keys()[0]]
    max_name = similarity.keys()[0]
    for name in similarity.keys():
        if(similarity[name]> max):
            max_name = name
            max = similarity[name]
    return max_name

def least_simillar(mp, votes):
    similarity = {}
    for member in votes.keys():
        if(not member == mp):
            similarity[member] = policy_compare(mp, member, votes)
    min = similarity[similarity.keys()[0]]
    min_name = similarity.keys()[0]

    for name in similarity.keys():
        if(similarity[name] < min):
            min_name = name
            min = similarity[name]
    return min_name

def least_simillar_acrosee_all_policies(mp):
    least = []
    f = open("data_clean/result_clean.json")
    d = f.read()
    data = json.loads(d)
    least.append(least_simillar(mp,data))
    return least

def simillars_across_all_policies(mp):
    simillar = []
    f = open("data_clean/result_clean.json")
    d = f.read()
    data = json.loads(d)
    simillar.append(most_simillar(mp,data))
    return simillar

def putIntoHistogram(data):
    result = {}
    for name in data:
        if name in result.keys():
            result[name] = result[name] + 1
        else:
            result[name] = 0
    return result

def plot(hist):
    names = hist.keys()
    num_name = hist.values()
    xs = [i + 1 for i, _ in enumerate(names)]
    plt.bar(xs, num_name)

    plt.ylabel("# of Simillarities")
    plt.title("Similarity Graph")

    # label x-axis with movie names at bar centers
    plt.xticks([i + 0.5 for i, _ in enumerate(names)], names)

    plt.show()


#which two senators disagree the most
#which two senators have the lowest dot product
def bitter_rivals(data):
	d = {mp1+" "+mp2: policy_compare(mp1, mp2, data)  for mp1 in data.keys() for mp2 in data.keys() if not (mp1 == mp2)}
	minvalue = {"name":"some", "value": 0}
	for mp_pair in d.keys():
		if(minvalue["name"] == "some"):
			minvalue["value"] = d[mp_pair]
			minvalue["name"] = mp_pair
		elif(minvalue["value"] > d[mp_pair]):
			minvalue["value"] = d[mp_pair]
			minvalue["name"] = mp_pair
	return minvalue


def most_political_oponents(threshhold,data):
	

f = open("data_clean/result_clean.json")
data = f.read()
formatted_data = json.loads(data)
result = policy_compare("Mr. Ziad Aboultaif","Mr. Dan Vandal",formatted_data)
print "Degree of similarity: "+str(result)

mp = "Mr. Glen Motz"
print "Most simmilar to "+mp+": " + most_simillar(mp, formatted_data)
print "Least simillar to "+mp+": " + least_simillar(mp, formatted_data)
print "Simmilars across all votes for Mr. Romeo Saganash: "
overallSimilarities = least_simillar_acrosee_all_policies("Mr. Romeo Saganash")
print bitter_rivals(formatted_data)
