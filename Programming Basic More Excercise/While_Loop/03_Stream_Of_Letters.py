sc_latter1 = False
sc_latter2 = False
sc_latter3 = False

output = ''
current_word = ''

while True:
    if sc_latter1 and sc_latter2 and sc_latter3:
        output += current_word + ' '
        current_word = ''
        sc_latter1 = False
        sc_latter2 = False
        sc_latter3 = False

    letter_input = input()
    if letter_input == 'End':
        break

    ascii_char = ord(letter_input)
    if not(65 <= ascii_char <= 90 or 97 <= ascii_char <= 122):
        continue

    if letter_input == 'c' and not sc_latter1:
        sc_latter1 = True
        continue
    if letter_input == 'o' and not sc_latter2:
        sc_latter2 = True
        continue
    if letter_input == 'n' and not sc_latter3:
        sc_latter3 = True
        continue

    current_word += letter_input

print(output)
