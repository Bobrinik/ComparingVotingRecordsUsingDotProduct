# Comparing Voting Records Using Dot Product
This is an implementation of the lab described in "Coding the Matrix book"


# Theory behind this project
- What is a dot-product?
	- It is a scalar product of vectors
	- u * v = u[0] * v[0] + u[1] * v[1] + u[2] * v[2] + ... + u[n] * v[n] 
- How can we use dot-product?
	-It can be used to measure the simillarity between vetors over R

```
v1 = {'Mp1':[1,0,0]}
v2 = {'Mp2':[0,0,1]}
v3 = {'Mp3':[1,0,0]}
v1 * v2 == 0
v1 * v3 == 1
```


# Implementation

## Data used:

1. http://www.parl.gc.ca/HouseChamberBusiness/Chambervotedetail.aspx?Language=E&Mode=1&Parl=42&Ses=2&FltrParl=42&FltrSes=1&vote=1
  * Voting vectors can be scrapped from the website above
2. http://www.parl.gc.ca/parliamentarians/en/members
  * Members of Parliment can be found here


- Python script to scrap data from the website is getVotes.py
- Python script to put data in a more friendly format is in put_in_one_file.py
- Python script to process data is in process.py


Data structure for implementation to work:

```javascript
//after getVotes.py
{"votes": [{"name": "Mr. Ziad Aboultaif", "party": "Conservative", "votes": {"nay": 1, "paired": 0, "yea": 0}}, {"name": "Mr. Harold Albrecht", "party": "Conservative", "votes": {"nay": 1, "paired": 0, "yea": 0}}, {"name": "Mr. John Aldag", "party": "Liberal", "votes": {"nay": 1, "paired": 0, "yea": 0}}, {"name": "Mr. Omar Alghabra", "party": "Liberal", "votes": {"nay": 1, "paired": 0, "yea": 0}}]}

//after clean.py 

{"Mr. Gary Anandasangaree": {"yea": 1, "paired": 0, "nay": 0}, ...}
creates a separate file with cleaned data per policy
```
