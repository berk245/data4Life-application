from pymongo import MongoClient
from pprint import pprint

client = MongoClient(
    "mongodb+srv://test_user:test1234@cluster0-f50l9.mongodb.net/d4Life?retryWrites=true&w=majority")
db = client.d4Life

subscriberList = []
for i in range(1500000):
    if i % 3 == 0:
        subscribed = False
    else:
        subscribed = True

    newUser = {
        "name": "User {}".format(i),
        "email": "email{}@test.com".format(i),
        "subscribedToNewsletter": subscribed
    }
    subscriberList.append(newUser)

db.userList.insert_many(subscriberList)
