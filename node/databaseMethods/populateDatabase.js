const User = require("../databaseFunctions/UserModel");
const mongoose = require("mongoose");
require("dotenv/config");

mongoose.connect(
  process.env.DB_CONNECTION,
  { useNewUrlParser: true, useUnifiedTopology: true },
  () => {
    console.log("Connected to DB!");
  }
);
let userList = [];
async function bulks(base, limit) {
  for (let i = base; i < limit; i++) {
    let subscribed = true;
    if (i % 3 == 0) {
      subscribed = false;
    }
    const newUser = new User({
      name: "New User " + i,
      email: "email" + i + "@cc.com",
      subscribedToNewsletter: subscribed,
    });
    userList.push(newUser);
  }
}
//The function itself causes memory heap
//Some workarounds didn't work, like async await
//Currently done by manually changing params.. Will look for an ideal option later
bulks(1000000, 1500000);
User.collection.insertMany(userList, onInsert);

function onInsert(err) {
  if (err) {
    console.log(err);
  } else {
    console.log("All entries are inserted");
  }
}
