filePath = input().split(chr(92))

file_name, file_extension = filePath[-1].split(".")

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")