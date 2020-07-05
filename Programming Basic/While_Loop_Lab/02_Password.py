username = input()
password = input()

confirm_password = input()

while password != confirm_password:
    confirm_password = input()
print(f"Welcome {username}!")