import json
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
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

stats_dictionary = {"RATIO": [0,0,0,0,0,0,0,0]}

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

click_ratios = {
    "jobs": {},
    "cities": {},
    "education_levels": {},
    "martial_statuses": {},
    "genders": {}
}

for job in jobs:
    user_group = [user for user in users.values() if user["job"] == job]
    job_impression = [0,0,0,0,0,0,0,0]
    job_click = [0,0,0,0,0,0,0,0]
    for user in user_group:
        job_impression = [x + y for x, y in zip(user["IMPRESSION"], job_impression)]
        job_click = [x + y for x, y in zip(user["CLICK"], job_click)]
    click_ratios["jobs"][job] = [x / y if y != 0 else 0 for x, y in zip(job_click, job_impression)]

for city in cities:
    user_group = [user for user in users.values() if user["cityName"] == city]
    print(city, len(user_group))
    city_impression = [0,0,0,0,0,0,0,0]
    city_click = [0,0,0,0,0,0,0,0]
    for user in user_group:
        city_impression = [x + y for x, y in zip(user["IMPRESSION"], city_impression)]
        city_click = [x + y for x, y in zip(user["CLICK"], city_click)]
    click_ratios["cities"][city] = [x / y if y != 0 else 0 for x, y in zip(city_click, city_impression)]

for education_level in education_levels:
    user_group = [user for user in users.values() if user["education"] == education_level]
    print(education_level, len(user_group))
    education_level_impression = [0,0,0,0,0,0,0,0]
    education_level_click = [0,0,0,0,0,0,0,0]
    for user in user_group:
        education_level_impression = [x + y for x, y in zip(user["IMPRESSION"], education_level_impression)]
        education_level_click = [x + y for x, y in zip(user["CLICK"], education_level_click)]
    click_ratios["education_levels"][education_level] = [x / y if y != 0 else 0 for x, y in zip(education_level_click, education_level_impression)]

for martial_status in martial_statuses:
    user_group = [user for user in users.values() if user["martialStatus"] == martial_status]
    print(martial_status, len(user_group))
    martial_status_impression = [0,0,0,0,0,0,0,0]
    martial_status_click = [0,0,0,0,0,0,0,0]
    for user in user_group:
        martial_status_impression = [x + y for x, y in zip(user["IMPRESSION"], martial_status_impression)]
        martial_status_click = [x + y for x, y in zip(user["CLICK"], martial_status_click)]
    click_ratios["martial_statuses"][martial_status] = [x / y if y != 0 else 0 for x, y in zip(martial_status_click, martial_status_impression)]

for gender in genders:
    user_group = [user for user in users.values() if user["gender"] == gender]
    gender_impression = [0,0,0,0,0,0,0,0]
    gender_click = [0,0,0,0,0,0,0,0]
    for user in user_group:
        gender_impression = [x + y for x, y in zip(user["IMPRESSION"], gender_impression)]
        gender_click = [x + y for x, y in zip(user["CLICK"], gender_click)]
    click_ratios["genders"][gender] = [x / y if y != 0 else 0 for x, y in zip(gender_click, gender_impression)]

plt.figure(figsize=(19.2, 10.8), dpi=100)
for job in jobs:
    plt.title("Job - Click Time Graph")
    plt.ylabel("Click/Impression Rate")
    plt.xlabel("Time")
    plt.plot(["00-03", "03-06", "06-09", "09-12", "12-15", "15-18", "18-21", "21-24"], click_ratios["jobs"][job], label=job)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
pylab.savefig("./plots/" + "jobs" + ".png", bbox_inches="tight")
plt.clf()

plt.figure(figsize=(19.2, 10.8), dpi=100)
for city in cities:
    plt.title("City - Click Time Graph")
    plt.ylabel("Click/Impression Rate")
    plt.xlabel("Time")
    plt.plot(["00-03", "03-06", "06-09", "09-12", "12-15", "15-18", "18-21", "21-24"], click_ratios["cities"][city], label=city)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
pylab.savefig("./plots/" + "cities" + ".png", bbox_inches="tight")
plt.clf()

plt.figure(figsize=(19.2, 10.8), dpi=100)
for martial_status in martial_statuses:
    plt.title("Mrtial Statuses - Click Time Graph")
    plt.ylabel("Click/Impression Rate")
    plt.xlabel("Time")
    plt.plot(["00-03", "03-06", "06-09", "09-12", "12-15", "15-18", "18-21", "21-24"], click_ratios["martial_statuses"][martial_status], label=martial_status)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
pylab.savefig("./plots/" + "martial_statuses" + ".png", bbox_inches="tight")
plt.clf()

plt.figure(figsize=(19.2, 10.8), dpi=100)
for education_level in education_levels:
    plt.title("Education Level - Click Time Graph")
    plt.ylabel("Click/Impression Rate")
    plt.xlabel("Time")
    plt.plot(["00-03", "03-06", "06-09", "09-12", "12-15", "15-18", "18-21", "21-24"], click_ratios["education_levels"][education_level], label=education_level)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
pylab.savefig("./plots/" + "education_levels" + ".png", bbox_inches="tight")
plt.clf()

plt.figure(figsize=(19.2, 10.8), dpi=100)
for gender in genders:
    plt.title("gender - Click Time Graph")
    plt.ylabel("Click/Impression Rate")
    plt.xlabel("Time")
    plt.plot(["00-03", "03-06", "06-09", "09-12", "12-15", "15-18", "18-21", "21-24"], click_ratios["genders"][gender], label=gender)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
pylab.savefig("./plots/" + "genders" + ".png", bbox_inches="tight")
plt.clf()