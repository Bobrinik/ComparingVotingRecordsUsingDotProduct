import json

def dot_product(vote1, vote2):
    result = [product(v1,v2) for v1 in vote1  for v2 in vote2]
    sum = 0
    for i in result:
        sum = sum + i
    return sum

def product(vote1, vote2):
    return vote1['nay']*vote2['nay']+vote1['paired']*vote2['paired']+vote1['yea']*vote2['yea']

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

f = open("data/data.json")
data = f.read()
formatted_data = json.loads(data)
result = policy_compare("Mr. Ziad Aboultaif","Mr. Dan Vandal",formatted_data)
print "Degree of similarity: "+str(result)
print "Most simmilar to Mr. Phil McColeman: " + most_simillar("Mr. Phil McColeman", formatted_data)
print "Least simillar to Mr. Phil McColeman: " + least_simillar("Mr. Phil McColeman", formatted_data)