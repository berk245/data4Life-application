1. Approach & Summary

   The challenge I have received asks me to write a program that will send out emails to recipients
   from a huge list (1 Mio entries) in a performant way. I wanted to include couple more small features, to
   make my solution a bit more relevant to a potential real-world use case.

   The main idea here was that the big list of recipients has to be retrieved from some source before it is handled. In my case, the mail
   addresses come from an external database that consists 1.500.000 users, 1.000.000 of which are subscribers of a newsletter,
   which is hypothetically the reason for sending the e-mail. (The methods used to populate the database can be seen in the
   populateDatabase.py file.)

   After retrieving the subscribed users, the app sends a personalized mail to each user / mocks the sending process.

2. Process

   I have started developing the application using node.js. However, due to some memory heaps and performance issues (both at populating and
   reading from the database), I decided to switch to Python. My node.js code is also included in the repository, if you'd like to have
   a look at it.

   The app is able to populate and retrieve data from the database(MongoDB). I have included a SMTP library to imitate the process of
   mail sending, with a test Gmail account. The problem was that Gmail blocks the application after sending 140 emails and this is a small sample
   when the entire million tasks are considered.

   Therefore, I have created another function, mock_mail_sender, which only prints a statement with a delay of half a second (as suggested in the original challenge).
   To increase the performance and the time elapsed, the application has the multiprocessing enabled, which takes advantage of all available processing units of the
   computer it is executed in.

3. Issues & Possible improvements

   a. The access information for database and mail address are not hidden and does not use a .env file or
   Environment variables. This is a decision I made, in case you would like to test the application with my test accounts.

   b. Although multiprocessing increases the speed of application, due to the immense amount of tasks it does, it still requires a lot
   of time. I will make a research on the possibility of implementing more sophisticated methods or combination of methods to further decrease the runtime.

4. Learnings

   While trying to develop the app using node.js, I have encountered problems and approaches to fix those problems that I have
   yet to have much experience with. Memory heap, threading and working threads, streams are some to mention. Although I have implemented a solution with multiprocessing to
   overcome some of these issues, I still need to dive deeper to get a better comprehension on the subject and the best practices.
