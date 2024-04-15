class Comment:  # a class called 'Comment'. We can call it however we like

    def __init__(self, username, content, likes=0):     # initializes the attributes
        self.username = username
        self.content = content          # then every single attribute should be submitted like this
        self.likes = likes              # self.{attribute_name} = attribute


comment = Comment("user1", "I like this book")

print(comment.username)
print(comment.content)
print(comment.likes)
