<<<<<<< HEAD
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
=======
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
>>>>>>> 06f2e621b68de7dbe64b4c1441e71917f616ece7
