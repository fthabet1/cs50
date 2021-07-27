people = [
    {"name": "Luffy", "fruit": "Gum-Gum"},
    {"name": "Ace", "fruit": "Flame-Flame"},
    {"name": "Brook", "fruit": "Revive-Revive"}
]

people.sort(key=lambda person: person["name"])

print(people)
