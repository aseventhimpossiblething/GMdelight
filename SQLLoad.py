print("pre import sql")
import sqlite3
import pandas

def MakeDailyTable(x):
    x=x.drop(columns=['index'])
    novelXstr="";
    y=x.columns;
    print("Make Data Input")
    for elem in y:
        elem=elem+" REAL, ";
        novelXstr=novelXstr+elem;
    novelXstr=novelXstr[:len(novelXstr)-1]     
    novelXstr2="create table DailyTable("+novelXstr[:len(novelXstr)-1]+");" 
    novelXstr3=novelXstr.replace(" REAL","");
    novelXstr3=novelXstr3[:len(novelXstr3)-1];
    
    insertionCols=novelXstr
    insert="insert into DailyTable() Values()"
    query="select*from DailyTable"
    SQLite3conn=sqlite3.connect("DailyDB")
    cursor=SQLite3conn.cursor();
    cursor.execute(novelXstr2);
     
    rowcount=0;
    while rowcount<len(x):
          print("start cycle-------------");
          littleStr="";       
          littlecount=0;
          while littlecount<len(x.iloc[rowcount]):
                littleStr=littleStr+str(x.iloc[rowcount][littlecount])+","
                littlecount=littlecount+1;
                            
          print(type(x.iloc[rowcount]),"-",x.iloc[rowcount]);
          littleStr=littleStr[:len(littleStr)-1]
          print("littleStr-",littleStr)
          insertionOrder="insert into DailyTable("+novelXstr3+") Values("+littleStr+")"  
          cursor.execute(insertionOrder);
          print("end cycle-------------");  
          rowcount=rowcount+1;
    
    
    
   
    cursor.execute(query);
    results=cursor.fetchall();
    print("results",results)
    print(x)
    print("novelXstr",novelXstr)
    print("novelXstr2",novelXstr2)
    print("novelXstr3",novelXstr3)
   
    
    print("end Make Daily")
    
    

    
    

