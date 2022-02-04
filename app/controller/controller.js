const { request } = require("express");
const db = require("../models");
const ItemsDB = db.items;
// used to search strings in the title column of the items table
const Op = db.Sequelize.Op;

exports.testing = (req, res) => {
  let message = "this route is now working!!!";
  res.json({ test: message });
};

exports.findOne = (req, res) => {
  const id = req.params.id;

  // ItemsDB.findOne({
  //   where: {
  //     id: id,
  //   },
  // })
  //   .then((item) => {
  //     res.json(item);
  //   })
  //   .catch((err) => {
  //     res.status(500).json(err);
  //   });

  // check if the query param for title exists and then query accordingly.
  // const query_title = req.query.title;
  // if (query_title) {
  //   console.log("Look here == === === === " + query_title);
  //   ItemsDB.findOne({
  //     where: {
  //       title: query_title,
  //     },
  //   }).then((item) => {
  //     res.json(item);
  //   }).catch ((err) => {
  //     res.status(500).json(err);
  //   }
  //   )
  // }

  ItemsDB.findByPk(id)
    .then((data) => {
      res.send(data);
    })
    .catch((err) => {
      res.status(500).send({ message: err.message });
    });
};

exports.find_title = (req, res) => {
  const id = req.params.id;

  ItemsDB.findAll({
    where: {
      id: id,
    },
    attributes: ["title"],
  })
    .then((item) => {
      res.send(item);
    })
    .catch((err) => res.status(500).send(err));
};

exports.delete = (req, res) => {
  const id = req.params.id;
  ItemsDB.destroy({
    where: {
      id: id,
    },
  })
    .then((data) => {
      if (data == 1) {
        res.send({ message: "Item is now deleted" });
      }
    })
    .catch((err) => {
      res.status(500).send({ message: err.message });
    });
};
