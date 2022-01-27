const db = require("./db");

const getItems = (req, res) => {
  res.json({ message: "Testing new endpoint to fetch all the items." });
};


module.exports = {
    getItems,
};