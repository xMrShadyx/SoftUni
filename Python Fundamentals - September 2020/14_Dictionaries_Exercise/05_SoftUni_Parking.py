n = int(input())
my_dict = {}

for _ in range (n):
    line = input()
    text = line.split()
    command = text[0]
    name = text[1]

    if command == "register":
        if not name in my_dict:
            my_dict[name] = text[2]
            print(f"{name} registered {my_dict[name]} successfully")
        else:
            print(f"ERROR: already registered with plate number {my_dict[name]}")
    elif command == "unregister":
        if name in my_dict:
            print(f"{name} unregistered successfully")
            my_dict.pop(name)
        else:
            print(f"ERROR: user {name} not found")

for key,value in my_dict.items():
    print(f"{key} => {value}")
