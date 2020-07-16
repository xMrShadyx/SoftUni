import math

word = input()

list_of_w = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
summ = 0
max_sum = 0
the_word = ""

while word != "End of words":
    for i in word:
        summ += ord(i)

    if word[0] in list_of_w:
        summ = summ * len(word)
    else:
        summ = math.floor(summ / len(word))

    if summ > max_sum:
        max_sum = summ
        the_word = word

    summ = 0
    word = input()
else:
    print(f"The most powerful word is {the_word} - {max_sum}")