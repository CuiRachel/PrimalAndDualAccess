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

3. If the column type of origin is "text" or "character varying", minor changes are needed to run the script (commented in the script);

4. The default time threshold setting is [1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000] opportunities, which can be edited;

5. The output will be named as "dual_access" stored in the same schema as the travel time matrix and opportunities tables in PgAdmin.

## ArcGIS Model

We built a model based on ArcGIS Model Builder to run the network analyst tool in loop to calculate travel time matrices.

If the numbers of origins and destinations are quite small, the OD cost matrix can be directly built following the steps described in http://desktop.arcgis.com/en/arcmap/latest/extensions/network-analyst/od-cost-matrix.htm;

If the numbers of origins and destinations are large, ArcGIS cannot solve the matrix due to the memory limitation, which requires to separate the origins/destinations and run the tool in loop to fill the matrix. 

Note that, one more step need to be done for transit travel time calculations before running the network analyst tool, that is adding GTFS data to a network dataset. The details are shown in https://esri.github.io/public-transit-tools/AddGTFStoaNetworkDataset.html.

