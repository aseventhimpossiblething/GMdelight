print("pre import sql")
import sqlite3
import pandas

def MakeDailyTable(x):
    novelXstr="";
    x=x.columns;
    print("Make Data Input")
    #print(x) 
    #print(len(x))
    for elem in x:
        elem=elem+" REAL, ";
        novelXstr=novelXstr+elem;
        #novelXarr.append(elem)
    novelXstr=novelXstr[:len(novelXstr)-1]     
    novelXstr="create table DailyTable("+novelXstr[:len(novelXstr)-1]+");" 
    novelXstr=novelXstr.replace("index REAL,","")
    #print("length of x");
    #print(len(x));
    #print("length of new arr");
    #print(len(novelXarr))
    print(novelXstr)
    
    query="select*from DailyTable"
    SQLite3conn=sqlite3.connect("DailyDB")
    cursor=SQLite3conn.cursor();
    cursor.execute(novelXstr);
    cursor.execute(query);
    
    results=cursor.fetchall();
    
    print("end Make Daily")
    
    

    
    
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
