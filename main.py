import json
import os

if os.path.exists("sessions.json"):
    with open("sessions.json", "r") as file:
        sessions = json.load(file)
else:
    sessions = []


topic = input("What did you study? ")
minutes = int(input("How many minutes did you study? "))


session = {
    "topic": topic,
    "minutes": minutes
}


sessions.append(session)


with open("sessions.json", "w") as file:
    json.dump(sessions, file, indent=4)

print(f"You studied {topic} for {minutes} minutes.")