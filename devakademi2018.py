import json
from datetime import datetime

# open the file that contains the data
with open("./all_data 3.json", encoding='utf-8') as file:
    data = json.loads(file.read())

users = {}

# Iterate over all items in data set
for item in data:
    timestamp = item["event_date"]
    user_id = item["viewer_user_id"]
    event_type = item["event_type"]

    # Ignore corrupted data
    if timestamp is None or event_type is "" or event_type is None:
        continue

    # Create a key for user if it does not exist
    if user_id not in users:
        users[user_id] = {
            "IMPRESSION": [0,0,0,0],
            "CLICK": [0,0,0,0]
        }

    # Extract hour from item
    readible_time = str(datetime.fromtimestamp(int(timestamp)))
    hour = (readible_time.split(" ")[1][0:2])
    
    # Add score to time groups of user according to hour
    if ("00" <= hour < "06"):
        users[user_id][event_type][0] = users[user_id][event_type][0] + 1
    elif ("06" <= hour < "12"):
        users[user_id][event_type][1] = users[user_id][event_type][1] + 1
    elif ("12" <= hour < "18"):
        users[user_id][event_type][2] = users[user_id][event_type][2] + 1
    elif ("18" <= hour < "24"):
        users[user_id][event_type][3] = users[user_id][event_type][3] + 1

print(json.dumps(users, indent=True))