print("pre import sql")
import sqlite3
import pandas

def MakeDailyTable(x):
    #print(x)
    x=x.drop(columns=['index'])
    #print(x)
    novelXstr="";
    y=x.columns;
    print("Make Data Input")
    for elem in y:
        elem=elem+" REAL, ";
        novelXstr=novelXstr+elem;
        #novelXarr.append(elem)
    novelXstr=novelXstr[:len(novelXstr)-1]     
    novelXstr="create table DailyTable("+novelXstr[:len(novelXstr)-1]+");" 
    novelXstr=novelXstr#.replace("index REAL,","")
    #print("length of x");
    #print(len(x));
    #print("length of new arr");
    #print(len(novelXarr))
    print(novelXstr)
    
    rowcount=0;
    while rowcount<len(x):
    #for elemen in x:
          print(x.iloc[rowcount]);
          #print(z.iloc([0]));  
          #print(z.iloc([1])); 
          #print(x[rowcount]);
          rowcount=rowcount+1;
    
    insert="insert into DailyTable() Values()"
    query="select*from DailyTable"
    SQLite3conn=sqlite3.connect("DailyDB")
    cursor=SQLite3conn.cursor();
    cursor.execute(novelXstr);
    cursor.execute(query);
    
    results=cursor.fetchall();
    print("results",results)
    print(x)
    #print(z.iloc[0])
    
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
