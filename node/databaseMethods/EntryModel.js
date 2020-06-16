const mongoose = require("mongoose");

const UserSchema = mongoose.Schema({
  name: String,
  email: String,
  subscribedToNewsletter: Boolean,
});

module.exports = mongoose.model("Users", UserSchema);
