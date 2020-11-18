
is_active = True
while is_active:
    text = input()
    if text == "end":
        is_active = False
        break
    text_reversed = ''

    for ch in reversed(text):
        text_reversed += ch
    print(text + " = " + text_reversed)
