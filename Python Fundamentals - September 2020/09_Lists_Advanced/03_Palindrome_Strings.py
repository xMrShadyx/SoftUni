word = input().split()
searched_word = input()


palindroms = [words for words in word if words == words[::-1]]
occ = palindroms.count(searched_word)
print(palindroms)
print(f"Found palindrome {occ} times")