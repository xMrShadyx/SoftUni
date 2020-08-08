def is_palindrome(word):
    return word == word[::-1]


words = input().split(' ')
search_palindrome = input()

palindromes = [word for word in words if is_palindrome(word)]

print(palindromes)
print(f"Found palindromes {palindromes.count(search_palindrome)} times")
