# PrimalAndDualAccess

## Primal-Access.py

This is a python script that calls PostgreSQL for primal accessibility calculations. The required inputs include tables of travel time matrix and opportunity stored in PgAdmin. The table names and column names need to be defined in the script.

The default time threshold setting is [10,20,30,40,50,60] minutes, which can be edited in the script.

The output will be named as "primal_access" stored in the same schema as the travel time matrix and opportunities tables in PgAdmin.
