line = input()
users = {}
languages = {}
while line != "exam finished":

    if "banned" in line:
        name, banned = line.split("-")
        if name in users:
            users.pop(name)
    else:
        name, language, points = line.split("-")
        points = int(points)
        if name not in users:
            users[name] = []
        users[name].append(points)
        if language not in languages:
            languages[language] = 0
        languages[language] += 1

    line = input()
users = {key: max(value) for key,value in users.items()}
users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
languages = dict(sorted(languages.items(), key=lambda x: (-x[1], x[0])))

print(f"Results:")
for key, value in users.items():
    print(f"{key} | {value}")
print(f"Submissions:")
for key,value in languages.items():
    print(f"{key} - {value}")
