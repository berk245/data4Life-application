const Post = require("../databaseFunctions/Models/Post");
const mongoose = require("mongoose");
require("dotenv/config");
const bodyParser = require("body-parser");

mongoose.connect(
  process.env.DB_CONNECTION,
  { useNewUrlParser: true, useUnifiedTopology: true },
  () => {
    console.log("Connected to DB!");
  }
);
async function getUsers() {
  try {
    const users = JSON.parse(await Post.find({ subscribedToNewsletter: true }));
    console.log(typeof users);
  } catch (err) {
    console.log(err);
  }
}

getUsers();
