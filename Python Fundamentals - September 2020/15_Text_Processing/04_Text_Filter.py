banned_words = input().split(", ")
random_text = input()

for word in banned_words:
    while word in random_text:
        random_text = random_text.replace(word, "*" * len(word))
print(random_text)
