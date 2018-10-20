import json
from datetime import datetime

# open the file that contains the data
with open("./all_data.json", encoding='utf-8') as file:
    all_data = json.loads(file.read())

with open("./user_data.json", encoding='utf-8') as file:
    users = json.loads(file.read())

for user in users:
    user["IMPRESSION"] = [0,0,0,0,0,0,0,0]
    user["CLICK"] = [0,0,0,0,0,0,0,0]

users = {user["id"]:user for user in users}

# Iterate over all items in data set
for item in all_data:
    timestamp = item["event_date"]
    user_id = item["viewer_user_id"]
    event_type = item["event_type"]

    # Ignore corrupted data
    if timestamp is None or event_type is "" or event_type is None:
        continue

    # Extract hour from item
    readible_time = str(datetime.fromtimestamp(int(timestamp)))
    hour = (readible_time.split(" ")[1][0:2])
    
    # Add score to time groups of user according to hour
    if ("00" <= hour < "03"):
        users[user_id][event_type][0] = users[user_id][event_type][0] + 1
    elif ("03" <= hour < "06"):
        users[user_id][event_type][1] = users[user_id][event_type][1] + 1
    elif ("06" <= hour < "09"):
        users[user_id][event_type][2] = users[user_id][event_type][2] + 1
    elif ("09" <= hour < "12"):
        users[user_id][event_type][3] = users[user_id][event_type][3] + 1
    elif ("12" <= hour < "15"):
        users[user_id][event_type][4] = users[user_id][event_type][4] + 1
    elif ("15" <= hour < "18"):
        users[user_id][event_type][5] = users[user_id][event_type][5] + 1
    elif ("18" <= hour < "21"):
        users[user_id][event_type][6] = users[user_id][event_type][6] + 1
    elif ("21" <= hour < "24"):
        users[user_id][event_type][7] = users[user_id][event_type][7] + 1

stats_dictionary = {"IMPRESSION": [0,0,0,0,0,0,0,0], "CLICK": [0,0,0,0,0,0,0,0]}

jobs = set([user["job"] for uid,user in users.items()])
jobs = {job:stats_dictionary for job in jobs if job != ''}

cities = set([user["cityName"] for uid,user in users.items()])
cities = {city:stats_dictionary for city in cities if city != ''}

education_levels = set([user["education"] for uid,user in users.items()])
education_levels = {education_level:stats_dictionary for education_level in education_levels if education_level != ''}

martial_statuses = set([user["martialStatus"] for uid,user in users.items()])
martial_statuses = {martial_status:stats_dictionary for martial_status in martial_statuses if martial_status != ''}

genders = set([user["gender"] for uid,user in users.items()])
genders = {gender:stats_dictionary for gender in genders if gender != ''}

for job in jobs:
    user_group = [user for user in users.values() if user["job"] == job]
    for user in user_group:
        jobs[job]["IMPRESSION"] = [x + y for x, y in zip(jobs[job]["IMPRESSION"], user["IMPRESSION"])]
        jobs[job]["CLICK"] = [x + y for x, y in zip(jobs[job]["CLICK"], user["CLICK"])]
    jobs[job]["RATIO"] = [x / y if y != 0 else 0 for x, y in zip(jobs[job]["CLICK"], jobs[job]["IMPRESSION"])]

for city in cities:
    user_group = [user for user in users.values() if user["cityName"] == city]
    for user in user_group:
        cities[city]["IMPRESSION"] = [x + y for x, y in zip(cities[city]["IMPRESSION"], user["IMPRESSION"])]
        cities[city]["CLICK"] = [x + y for x, y in zip(cities[city]["CLICK"], user["CLICK"])]
    cities[city]["RATIO"] = [x / y if y != 0 else 0 for x, y in zip(cities[city]["CLICK"], cities[city]["IMPRESSION"])]

for education_level in education_levels:
    user_group = [user for user in users.values() if user["education"] == education_level]
    for user in user_group:
        education_levels[education_level]["IMPRESSION"] = [x + y for x, y in zip(education_levels[education_level]["IMPRESSION"], user["IMPRESSION"])]
        education_levels[education_level]["CLICK"] = [x + y for x, y in zip(education_levels[education_level]["CLICK"], user["CLICK"])]
    education_levels[education_level]["RATIO"] = [x / y if y != 0 else 0 for x, y in zip(education_levels[education_level]["CLICK"], education_levels[education_level]["IMPRESSION"])]

for gender in genders:
    user_group = [user for user in users.values() if user["gender"] == gender]
    for user in user_group:
        genders[gender]["IMPRESSION"] = [x + y for x, y in zip(genders[gender]["IMPRESSION"], user["IMPRESSION"])]
        genders[gender]["CLICK"] = [x + y for x, y in zip(genders[gender]["CLICK"], user["CLICK"])]
    genders[gender]["RATIO"] = [x / y if y != 0 else 0 for x, y in zip(genders[gender]["CLICK"], genders[gender]["IMPRESSION"])]

