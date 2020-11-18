line = input()
company = {}
while line != "End":
    name, id = line.split(" -> ")

    if name not in company:
        company[name] = []
    if id not in company[name]:
        company[name].append(id)

    line = input()
company = dict(sorted(company.items()))
for key, value in company.items():
    print(key)
    for i in value:
        print(f"-- {i}")
