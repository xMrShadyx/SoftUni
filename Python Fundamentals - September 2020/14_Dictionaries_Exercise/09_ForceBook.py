force = {}
users = {}
line = input()
while line != "Lumpawaroo":

    if "|" in line:
        side,user = line.split(" | ")
        if user not in users:
            users[user] = side

    elif "-" in line:
        user,side = line.split(" -> ")
        users[user] = side
        print(f"{user} joins the {side} side!")

    line = input()

for key, value in users.items():
    if value not in force:
        force[value] = []
    force[value].append(key)


force = dict(sorted(force.items(), key=lambda x : (-len(x[1]), x[0])))
for key, value in force.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for i in sorted(value):
            print(f"! {i}")
