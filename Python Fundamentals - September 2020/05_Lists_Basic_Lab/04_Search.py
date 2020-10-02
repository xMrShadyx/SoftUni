n = int(input())
word = input()

sentences_with_word = []
sentences_with_out = []

for i in range(n):
    text = input()
    if word in text:
        sentences_with_word.append(text)
        sentences_with_out.append(text)
    else:
        sentences_with_out.append(text)

print(sentences_with_out)
print(sentences_with_word)