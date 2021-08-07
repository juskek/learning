SQL is a querying language
Postgres is a database engine


# Data Structure
## Schema
### Table
#### Columns
#### Records

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
OR
`SELECT column_name FROM table_name GROUP BY column_name;`

Count occurences of a value in a column
`SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;`

Show values which have occurences fulfilling a condition
```
    SELECT column_name, COUNT(*) FROM table_name 
    GROUP BY column_name
    HAVING COUNT(*) OPERATOR CONDITION
```

Filter based on conditions (WHERE, AND, OR):
```
    SELECT * FROM table_name 
    WHERE column_name = column_value
    AND (column_name = column_value OR column_name = column_value);
```

Filter based on multiple conditions (IN)
```
    SELECT * FROM table_name
    WHERE column_name IN (condition1,condition2,...);
```

Filter between two conditions (BETWEEN)
```
    SELECT * FROM table_name
    WHERE column_name
    BETWEEN condition1 AND condition2
```

Filter based on similar characters (LIKE)
`SELECT * FROM table_name WHERE column_name LIKE '%character%'`
- %: wildcard, can take on any character(s)
- _: underscore, define number of characters
- ILIKE: non-case sensitive



Selecting first few rows 
`SELECT * FROM table_name LIMIT number_of_rows`
OR
`SELECT * FROM table_name FETCH FIRST number_of_rows ROW ONLY`


Selecting specific rows
`SELECT * FROM table_name OFFSET startnumber-1 LIMIT number_of_rows`

Selecting max/min/avg
`SELECT ROUND(MAX(column_name)) FROM table_name`

Summing values
`SELECT SUM(column_name) FROM table_name;`

Renaming columns (ALIAS)
`SELECT column_name AS new_name FROM table_name`

Replacing null value (COALESCE)
`SELECT COALESCE(column_name, <Default value if value is null>) FROM table_name;`

Return NULL for a specific condition (NULLIF)
`SELECT NULLIF(column_value,condition);`

Adding/subtracting dates
`SELECT NOW() - INTERVAL 'value DURATION';`

Casting dates
`SELECT NOW()::DATATYPE;`

Extracting date components
`SELECT EXTRACT(DATECOMPONENT FROM NOW());`



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

Adding primary key
`ALTER TABLE table_name ADD PRIMARY KEY (column_name1, column_name2)`

Dropping primary key
`ALTER TABLE table_name DROP CONSTRAINT primary_key_name`

(DANGER) Deleting records
- all: `DELETE FROM table_name`
- conditional: `DELETE FROM table_name WHERE column_name = value`

Resetting BIGSERIAL 

Updating records
- all: `UPDATE table_name SET column_name1 = value1, column_name2 = value2`
- conditional: `UPDATE table_name SET column_name1 = value1 WHERE column_name2 = value2`

Handling conflicts in columns with constraints (ON CONFLICT DO)
- Do nothing: `COMMANDS ON CONFLICT column_name1,column_name2 DO NOTHING`
- Update/insert record if existing/non-existing: `COMMANDS ON CONFLICT column_name1,column_name2 DO UPDATE SET column_name3 = EXCLUDED.column_name3;`






Adding unique constraint (e.g., emails):
`ALTER TABLE table_name ADD CONSTRAINT column_constraint_name UNIQUE(column_name)`

Adding constraint on values allowed in a column
`ALTER TABLE table_name ADD CONSTRAINT constraint_name CHECK (column_name = value1 OR column_name = value2)`






# Keys
## Primary Keys
Used to identify a record

When primary and foreign key have the same name (USING)


## Foreign Keys
Used to reference a primary key in another table

Creating foreign keys:
1. Create primary key in one table
2. Go to other table and create foreign key:
   `foreign_key_name DATATYPE REFERENCES table_name (primary_key_name)`

Updating foreign keys:
`UPDATE table_name SET foreign_key_name = value1 WHERE primary_key_name = value2`
 


Combining two tables and creates a new table of records with primary and foreign keys in both tables (Inner Joins = Union)

```
    SELECT table_name1.column_name, table_name2.column_name FROM table_name1
    JOIN table_name2 ON table_name1.foreign_key_name = table_name2.primary_key_name
```




Combining two tables by keeping all records of first table and records of second table with foreign keys in the first table (Left Joins)
```
    SELECT * FROM table_name1
    LEFT JOIN table_name2 ON table_name2.primary_key_name = table_name1.foreign_key_name
```
OR 

```
    SELECT  * FROM table_name1
    LEFT JOIN table_name2 USING primary_key_name
```

Deleting records with foreign keys referenced in another table
- Delete record
- Set foreign key to null

Exporting query results to CSV
```
    \copy 
    SELECT * FROM table_name
    TO
    'path_name/file_name.csv'
    DELIMITER ','
    CSV HEADER;
```

Extensions
- Show all/installed extensions: `SELECT * FROM pg_available_extensions;`
- Installing extensions: `CREATE EXTENSION IF NOT EXIISTS "extension_name"`




Universally Unique Identifier (GUID/UUID) 128-bit
- Good for primary keys, security
```
    CREATE TABLE table_name (
        table_uuid UUID NOT NULL PRIMARY KEY,
        ...
    )

    INSERT INTO table_name(table_uuid,...)
    VALUES (uuid_generate_v4(),...)
```