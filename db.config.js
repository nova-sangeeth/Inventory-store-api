module.exports = {
  HOST: "localhost",
  USER: "postgres",
  PASSWORD: "postgres",
  PORT: 7432,
  DB: "app",
  pool: {
    max: 120,
    min: 5,
    acquire: 30000,
    idle: 10000,
  },
};
