first_text = input()
second_text = input()

while first_text in second_text:
    second_text = second_text.replace(first_text, "")
print(second_text)
    
