1. Approach & Summary

   The challenge I have received asks me to write a program that will send out emails to recipients
   from a huge list (1 Mio entries) in a performant way. I wanted to include couple more small features, to
   make my solution a bit more relevant to a potential real-world usage.

   The main idea here was that the big list of recipients has to be retrieved from some source before it is handled. In my case, the mail
   addresses come from an external database that consists 1.500.000 users, 1.000.000 of which are subscribers of a newsletter,
   which is hypothetically the reason for sending the e-mail. (The methods used to populate the database can be seen in the
   populateDatabase.py file.)

   After retrieving the subscribed users, the app sends a personalized mail to each user.

2. Process

   I have started developing the application using node.js. However, due to some memory heaps and performance issues (both at populating and
   reading from the database), I decided to switch to Python. My node.js code is also included in the repository, if you'd like to have
   a look at it.

   The app is able to populate the database, retrieve data from the database(MongoDB) and send mails using a test Gmail account.

3. Issues & Possible improvements

   a. The access information for database and mail address are not hidden and does not use a .env file or
   Environment variables. This is a decision I made, in case you would like to test the application with my test accounts.

   b. GMail blocks the application after 140 mails. I made a quick research and found out that most of free mail service providers
   have a similar policy. I decided to keep it the way it is anyway, to actually send the mails instead of setting intervals.

4. Learnings

   While trying to develop the app using node.js, I have encountered problems and approaches to fix those problems that I have
   yet to have much experience with. Memory heap, threading and working threads, streams are some to mention. To use my time more efficiently,
   I decided to first try to write the same functions using Python, to see if there would be any improvements. Regardless of the result of
   my job application, I will dig deeper on those points and this is my biggest take away from this challenge.
