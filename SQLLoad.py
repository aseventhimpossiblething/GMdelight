print("pre import sql")
import sqlite3
import pandas

def MakeDailyTable(x):
    x=x.columns;
    print("Make Data Input")
    print(x) 
    print("end Make Daily")
    
    SQLite3conn=sqlite3.connect("DailyBD");
    cursor=SQLite3conn.cursor();
    queryP1="create table DailyTable("+x+")"
    #cursor.execute("create table DailyTable()");
    
    
"""
SQLite3conn=sqlite3.connect("DailyBD")
cursor=SQLite3conn.cursor();
cursor.execute("create table DailyTable")

b=cursor.execute("select*from DailyTable limit 1;")
c=ColNames=pandas.DataFrame(cursor.description)
c=c[[0]];

a=cursor.fetchall();

#print(cursor)
#print(cursor.description)
#print(SQLcolsnames)
print(a)
#print(b)
print(c)
print("post connect")
"""
