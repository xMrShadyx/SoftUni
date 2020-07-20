c = input()
b = ''

while c != 'End':

    new = str(c)
    for word in new:
        if word.isalpha():
            list = ['c', 'o', 'n']
            if word in list:
                list.remove(word)
            else:
                b += word
    c = input()


