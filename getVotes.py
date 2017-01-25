from bs4 import BeautifulSoup
import urllib
import json

def saveToFile(data, filename):
    target = open("data/" +filename+".json", "w")
    target.write(data)



def scrapData(url,name):
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r)
    print type(soup)
    vote_row = soup.find_all('tr', class_="detailsTableRow")
    vote_data = {}
    data = []
    try:
        vote_data['context'] = voteContext = soup.find('div', class_="voteContextArea").text
    except:
        print "Did not find context for"+str(name)
    vote_data['votes'] = data
    for element in vote_row:
        record = {}
        record['party'] = element.find('td', headers='Caucus').text
        record['name'] = element.find('a', class_='WebOption').text
        votes = {'yea':0, 'nay':0, 'paired':0}
        votes_raw = element.findAll('td', attrs={"class":"voteResultsCell"})
        if "img" in str(votes_raw[0]):
            votes['yea'] = 1
        elif "img" in str(votes_raw[1]):
            votes['nay'] = 1
        else:
            votes['paired'] = 1
        record['votes'] = votes
        data.append(record)
    saveToFile(json.dumps(vote_data, sort_keys=True), str(name))


url ="http://www.parl.gc.ca/HouseChamberBusiness/Chambervotedetail.aspx?Language=E&Mode=1&Parl=42&Ses=2&FltrParl=42&FltrSes=1&vote="
for i in range(55,183):
    scrapData(url+str(i),i)
    print "Finished vote:"+str(i)