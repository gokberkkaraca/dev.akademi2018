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