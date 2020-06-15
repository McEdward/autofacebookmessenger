import fbchat
from getpass import getpass

email = "Your email"
client = fbchat.Client(email, getpass())
name = "The persons full name as it appears on facebook"
baby = client.searchForUsers(name)
msg = "I love you"

for x in range(10000):
    sent = client.send(fbchat.models.Message(msg), baby[0].uid)
    if sent:
        print("Total messages sent: ", x)
