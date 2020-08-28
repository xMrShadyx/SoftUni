class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


content = Comment('Ico', 'I like this book', 54)

print(content.username)
print(content.content)
print(content.likes)
