# Comparing Voting Records Using Dot Product
This is an implementation of the lab described in "Coding the Matrix book"


# Theory behind this project
- What is a dot-product?
- How can we use dot-product?


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

//after put_one_file.py

{"Mr. Gary Anandasangaree": [{"yea": 1, "paired": 0, "nay": 0}, {"yea": 1, "paired": 0, "nay": 0}],"Mr. Steven Blaney": [{"yea": 0, "paired": 0, "nay": 1}, {"yea": 0, "paired": 0, "nay": 1}]}
```
