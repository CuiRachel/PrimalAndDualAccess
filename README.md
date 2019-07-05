# PrimalAndDualAccess

## Primal-Access.py

This is a python script that calls PostgreSQL for primal accessibility calculations. The required inputs include tables of travel time matrix and opportunity saved in PgAdmin. Note that,

1. Both tables should be saved in the same schema;

2. The table names and column names need to be defined in the script.

3. The default time threshold setting is [10,20,30,40,50,60] minutes, which can be edited in the script.

4. The output will be named as "primal_access" stored in the same schema as the travel time matrix and opportunities tables in PgAdmin.
