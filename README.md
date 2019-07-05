# PrimalAndDualAccess

## primal-access.py

This is a python script that calls PostgreSQL for primal accessibility calculations. The required inputs include tables of travel time matrix and opportunity saved in PgAdmin. Note that,

1. Both tables should be saved in the same schema;

2. The table names and column names need to be defined in the script;

3. The default time threshold setting is [10,20,30,40,50,60] minutes, which can be edited;

4. The output will be named as "primal_access" stored in the same schema as the travel time matrix and opportunities tables in PgAdmin.


## dual-access.py

This is a python script that calls PostgreSQL for dual accessibility calculations. The required inputs include tables of travel time matrix and opportunity saved in PgAdmin. Note that,

1. Both tables should be saved in the same schema;

2. The table names and column names need to be defined in the script;

3. The default time threshold setting is [1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000] opportunities, which can be edited;

4. The output will be named as "dual_access" stored in the same schema as the travel time matrix and opportunities tables in PgAdmin.
