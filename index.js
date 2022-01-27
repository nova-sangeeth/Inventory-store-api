const express = require("express");
const crud = require("./crud");
app = express();

app.get('/', (req, res) => {
    res.json({"message": req.method + "Testing the main URL " + req.url});
})

app.get('/items', crud.getItems);


app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
