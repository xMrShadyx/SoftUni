courses = {}
line = input()
while line != "end":
    course,student = line.split(" : ")
    if not course in courses:
        courses[course] = []
    courses[course].append(student)

    line = input()
courses = dict(sorted(courses.items(),key=lambda x: len(x[1]), reverse=True))
for key,value in courses.items():
    value.sort()
for key,value in courses.items():
    print(f"{key}: {len(value)}")
    for i in value:
        print(f"-- {i}")
