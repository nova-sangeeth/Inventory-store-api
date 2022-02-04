const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();

let corsOptions = {
    origin: "localhost:8080",
};

app.use(cors(corsOptions));

app.use(express.json());

app.use(express.urlencoded({ extended: true }));

const db = require("./app/models");

db.sequelize.sync({ force: true }).then(() => {
  console.log("Droping and re-syncing db.");
});

app.get("/", (req, res) => {
  message = "Hello There this is the message.";
  res.json({ Message: message });
});
require("./app/routes/items.routes")(app)
const port = 8080;

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
