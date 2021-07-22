

# PostgreSQL
Postgres is a service which needs to be started 
`brew services start postgresql`

Stopping the service when not needed frees up resources
`brew services stop postgresql`

Logging into postgres services
`psql postgres`

Creating new user
`CREATE ROLE justinkek WITH LOGIN PASSWORD 'password'`

Give user ability to create new databases
`ALTER ROLE justinkek CREATEDB`

Quit session
`\q`

Connect to session

List existing roles
`\du`
