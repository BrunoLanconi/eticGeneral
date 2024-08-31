# [Postgres](https://hub.docker.com/_/postgres)

## Commands

```bash
help                           Show help
up                             Run Postgres on port 5432 and Adminer on port 5433
```

## [Postgres](http://localhost:5432)

Postgres is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.

## [Adminer](http://localhost:5433)

Adminer is a full-featured database management tool written in PHP. Conversely to phpMyAdmin, it consist of a single file ready to deploy to the target server. Adminer is available for MySQL, MariaDB, PostgreSQL, SQLite, MS SQL, Oracle, Firebird, SimpleDB, Elasticsearch and MongoDB. To use it, you need to connect to the database using the following parameters:

```
System: PostgreSQL
Server: db
Username: user
Password: password
Database: db
```

Note that System is the type of database you are connecting to, Server is the name of the service in the docker-compose file, Username is the value of `POSTGRES_USER`, Password is the value of `POSTGRES_PASSWORD`, and Database is the value of `POSTGRES_DB`.