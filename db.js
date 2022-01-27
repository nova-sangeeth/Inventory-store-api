const ConnectionPool = require("pg").Pool;

const pool = new ConnectionPool({
  user: "postgres",
  host: "localhost",
  database: "postgres",
  password: "postgres",
  port: 5432,
});

