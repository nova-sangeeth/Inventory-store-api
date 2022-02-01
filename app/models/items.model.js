module.exports = (sequelize, Sequelize) => {
  const Items = sequelize.define("items", {
    title: {
      type: Sequelize.STRING,
    },
    brand: {
      type: Sequelize.STRING,
    }
  });
  return Items;
};
