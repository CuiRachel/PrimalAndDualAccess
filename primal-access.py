import csv
import os
import math
import time
import psycopg2 as pg


###################Inputs for the primal access calculation###############
#### ***** needs to be defined before running the script

conn = pg.connect("dbname=***** user=***** password=*****")
cur=conn.cursor()

schema="*****"   ### schema name

ttName="*****"  ### table name: travel time matrix
origColumn="*****" ### column name: origins
destColumn="*****" ### column name: destinations
ttColumn="*****" ### column name: travel time

oppName="*****" ### table name: opportunity
blockColumn="*****" ### column name: block ID
oppColumn="*****" ### column name: opportunity

thresholds=[10,20,30,40,50,60]

################### Functions ####################

def accessCal(ttName, ttTable, outputTableName,outputTable, thresholds):
    print("---Calculating accessibility matrix")
    cur.execute("select exists (select 1 from information_schema.tables where table_schema='{}' and table_name='{}')".format(schema, outputTableName))
    if cur.fetchone()[0]==False:
        cur.execute("select {} into {} from {} group by origin order by origin asc".format(origColumn, outputTable, ttTable))
        conn.commit()
    for i, threshold in enumerate(thresholds):
        print("threshold={}".format(threshold))
        columnName="access_{}min".format(threshold)
        cur.execute("alter table {} add column if not exists {} bigint".format(outputTable, columnName))
        cur.execute("update {} set {}=x.access from (select {}, sum({}) as access from {} where {}<={} group by {}) x where x.{}={}.{}".format(outputTable, columnName, origColumn, oppColumn, ttTable, ttColumn, threshold, origColumn, origColumn, outputTable, origColumn))
        conn.commit()


############ Primal access calculation #############

    
ttTable="{}.{}".format(schema, ttName)
oppTable="{}.{}".format(schema, oppName)
outputName="primal_access"
outputTable="{}.{}".format(schema, outputName)

ttOppName="{}_{}".format(ttName,oppColumn)
ttOppTable="{}.{}".format(schema, ttOppName)

startTime=time.time()

print("Join the tt table with the opp table")
cur.execute("select exists (select 1 from information_schema.tables where table_schema='{}' and table_name='{}')".format(schema, outputName))
if cur.fetchone()[0]==False:
    cur.execute("select x.{}, x.{}, x.{}, y.{} into {} from {} x left join {} y on x.{}=y.{}".format(origColumn, destColumn, ttColumn, oppColumn, ttOppTable, ttTable, oppTable, destColumn, blockColumn))
    conn.commit()

accessCal(ttName, ttTable, outputName, outputTable, thresholds)


endTime=time.time()
calTime=endTime-startTime

print("The accessibility calculation time is {}".format(calTime))

print("------------------Calculation Finished--------------")
