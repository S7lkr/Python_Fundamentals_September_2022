class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
line = input()

while line != 'Stop':
    sender, receiver, content = line.split()
    e_mail = Email(sender, receiver, content)   # e_mail is an 'object' with 3 arguments
    emails.append(e_mail)
    line = input()

sent_emails = [emails[int(index)].send() for index in input().split(', ')]
for email in emails:
    print(email.get_info())