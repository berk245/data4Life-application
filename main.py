import smtplib
from pymongo import MongoClient
from pprint import pprint
import time
import os
from multiprocessing import Process, current_process, Pool


def mail_sender(users):
    mailService = smtplib.SMTP("smtp.gmail.com", 587)
    mailService.starttls()
    mailService.login("absolutecream23@gmail.com", "TestPassword1234"),
    sender = "info@gmail.com"
    subject = "Hey There!"

    for user in users:
        msg = "Hello {}, we have got very good news for you!".format(
            user['name'])
        body = "Subject: {} \n\n {}".format(subject, msg)
        mailService.sendmail(sender, user['email'], body)
        print("Mail is sent to {} | {}".format(user['name'], user['email']))
    mailService.quit()


def mock_mail_sender(user):
    time.sleep(0.5)
    print(f"A mail is sent to {user['name']}")


def multiprocess_mail_sender(users):
    start_time = time.time()
    p = Pool()
    p.map(mock_mail_sender, users)
    p.close()
    p.join()
    end_time = time.time() - start_time
    print(f"Sending {len(users)} mails took {end_time}.")


if __name__ == '__main__':
    # Get the subscribed users from the database
    client = MongoClient(
        "mongodb+srv://test_user:test1234@cluster0-f50l9.mongodb.net/d4Life?retryWrites=true&w=majority")
    db = client.d4Life
    subscribed_users = list(db.userList.find({'subscribedToNewsletter': True}))
    multiprocess_mail_sender(subscribed_users)
