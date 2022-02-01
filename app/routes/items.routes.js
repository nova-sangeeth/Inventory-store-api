module.exports = (app) => {
  const items = require("../controller/controller.js");

  let router = require("express").Router();

  router.get("/get_items/:id", items.findOne);

  router.get("/get_title/:id", items.find_title);

  app.use("/api", router);
};
