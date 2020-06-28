import json
import random

#Reads and parses the Data of the file movieData.json
with open('movieData.json') as json_data:
    jsonData = json.load(json_data)

#Picks a random movie from the list
def pick_random():
    length = len(jsonData)
    rnd_index = random.randint(0,length)
    print(jsonData[rnd_index])
