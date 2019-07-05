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
destColumn="*****" ### column name: origins
ttColumn="*****" ### column name: travel time

oppName="*****" ### table name: opportunity
blockColumn="*****" ### column name: block ID
oppColumn="*****" ### column name: opportunity



thresholds=[1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000]

################### Functions ####################

def dualAccess(origin, input_table, output_table,thresholds):
    cur.execute("select {}, {}, {} from {} where {}={} order by {} asc".format(origColumn, ttColumn, oppColumn, input_table, origColumn, origin,ttColumn))  ### where {}={} -> where {}='{}' if column type of origin is text or character varying  
    ttOrigin=cur.fetchall()
    count_dest=len(ttOrigin)
    sumEmp=0
    num=0
    for thres in thresholds:
        while sumEmp<thres and num<=count_dest-1:
            sumEmp+=ttOrigin[num][2]
            num+=1
        if num>count_dest-1:
            accessValue=9999
        else:
            accessValue=ttOrigin[num-1][1]
        cur.execute("update {} set access_{}min={} where {}={}".format(output_table, thres, accessValue, origColumn, origin)) ### where {}={} -> where {}='{}' if column type of origin is text or character varying  
        conn.commit()   


############ Dual access calculation #############

    
ttTable="{}.{}".format(schema, ttName)
oppTable="{}.{}".format(schema, oppName)
outputName="dual_access"
outputTable="{}.{}".format(schema, outputName)

ttOppName="{}_{}".format(ttName,oppColumn)
ttOppTable="{}.{}".format(schema, ttOppName)

startTime=time.time()

cur.execute("create table if not exists {} ({} bigint)".format(outputTable, origColumn))
conn.commit()

for thres in thresholds:
    cur.execute("alter table  {} add column if not exists access_{}min double precision".format(outputTable, thres))
    conn.commit()

print("Join the tt table with the opp table")
cur.execute("select exists (select 1 from information_schema.tables where table_schema='{}' and table_name='{}')".format(schema, outputName))
if cur.fetchone()[0]==False:
    cur.execute("select x.{}, x.{}, x.{}, y.{} into {} from {} x left join {} y on x.{}=y.{}".format(origColumn, destColumn, ttColumn, oppColumn, ttOppTable, ttTable, oppTable, destColumn, blockColumn))
    conn.commit()

print("Calculating dual accessibility")

cur.execute("select {} from {} group by {}".format(origColumn, ttOppTable, origColumn))
origins=cur.fetchall()
for i, data in enumerate(origins):
    print("Calculating for origin {}".format(data[0]))
    cur.execute("insert into {} ({}) values ('{}')".format(outputTable,origColumn, data[0]))
    conn.commit()

    dualAccess(data[0], ttTable, outputTable, thresholds)


endTime=time.time()
calTime=endTime-startTime

print("The accessibility calculation time is {}".format(calTime))

print("------------------Calculation Finished--------------")
