import smtplib
from pymongo import MongoClient
from pprint import pprint

# The Task Manager shows a max value of ~440MB of RAM usage during
# data retrieval and mail sending processes


# Get the subscribed users from the database
client = MongoClient(
    "mongodb+srv://test_user:test1234@cluster0-f50l9.mongodb.net/d4Life?retryWrites=true&w=majority")
db = client.d4Life
subscribed_users = list(db.userList.find({'subscribedToNewsletter': True}))


mailService = smtplib.SMTP("smtp.gmail.com", 587)
mailService.starttls()
mailService.login("absolutecream23@gmail.com", "TestPassword1234"),
sender = "info@gmail.com"
subject = "Hey There!"

for user in subscribed_users:
    msg = "Hello {}, we have got very good news for you!".format(user['name'])
    body = "Subject: {} \n\n {}".format(subject, msg)
    mailService.sendmail(sender, user['email'], body)
    print("Mail is sent to {} | {}".format(user['name'], user['email']))
mailService.quit()
