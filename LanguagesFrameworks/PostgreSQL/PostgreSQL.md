SQL is a querying language
Postgres is a database engine


# Data Structure
## Schema
### Table
#### Rows
#### Columns

# Relational DB
When two or more tables are related.



# PostgreSQL
Postgres is a service which needs to be started 
`brew services start postgresql`

Stopping the service when not needed frees up resources
`brew services stop postgresql`

Logging into postgres services
`psql postgres`

# psql shell

Creating new user
`CREATE ROLE justinkek WITH LOGIN PASSWORD 'password'`

Give user ability to create new databases
`ALTER ROLE justinkek CREATEDB`

Quit session
`\q`

Connect to session

List existing roles
`\du`

List databases
`\l`

Create database
`CREATE DATABASE database_name;`

(DANGER): Delete
- database: `DROP DATABASE database_name;`
- table: `DROP DATABASE table_name;`

Create table
```
    CREATE TABLE table_name (
        id DATATYPE,
        column_name DATATYPE(constraints) constraints,
    );
```

Insert records into table
```
    INSERT INTO table_name (column_name,)
    VALUES (column_value,);
```

Show records from a column
`SELECT column_name FROM table_name;`

Order all records by a column
`SELECT * FROM table_name ORDER BY column_name ASC/DESC;`

Show distinct/unique values in a column
`SELECT DISTINCT column_name FROM table_name ORDER BY column_name ASC;`

Filter based on conditions (WHERE, AND, OR):
```
    SELECT * FROM table_name 
    WHERE column_name = column_value
    AND (column_name = column_value OR column_name = column_value);
```

Selecting first few rows 
`SELECT * FROM table_name LIMIT number_of_rows`
OR
`SELECT * FROM table_name FETCH FIRST number_of_rows ROW ONLY`


Selecting specific rows
`SELECT * FROM table_name OFFSET startnumber-1 LIMIT number_of_rows`



Execute commands from file
`\i <filepath>`



See all commands
`psql --help`

Connecting to a database
from shell: `psql -h host_name -p port_number -U user_name database_name`
OR
from psql shell: `psql` -> `\c database_name`

Describe
- database: `\d`
- table: `\d table_name`

