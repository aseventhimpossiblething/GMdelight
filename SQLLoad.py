print("pre import sql")
import sqlite3
import pandas
#import datetime
from datetime import date

print(date.today())



def addToTable(x):
    SQLite3conn=sqlite3.connect("DailyDB");
    cursor=SQLite3conn.cursor();
    cursor.execute();
    

def MakeDailyTable(z,a):
   
    a='"'+a+'"';
    curDate='"'+str(date.today())+'"'
    CurrentDate=[];
    symbolCol=[];
    for symb in z['index']:
        symbolCol.append(a);
        CurrentDate.append(curDate);
    z[['Symbol']]=symbolCol;
    z[['PredictionDay']]=CurrentDate;
    
    
        
    
    x=z.drop(columns=['index'])
    novelXstr="";
    y=x.columns;
    #print("Make Data Input")
    NewFrameTitles=[];
    for elem in y:
        strtest=str(type(x[elem][1]))+str(type(x[elem][2]))+str(type(x[elem][3]))+str(type(x[elem][4]))+str(type(x[elem][5]));
        if strtest.find('str')>-1:
           elem="'"+elem+"'"+" TEXT, ";
        else:
           elem="'"+elem+"'"+" REAL, ";
        novelXstr=novelXstr+elem;
    novelXstr=novelXstr[:len(novelXstr)-1];
    novelXstr2="create table DailyTable("+novelXstr[:len(novelXstr)-1]+");" 
    novelXstr3=novelXstr.replace(" REAL","");
    novelXstr3=novelXstr3.replace(" TEXT","");
    novelXstr3=novelXstr3.replace(" BLOB","");
    novelXstr3=novelXstr3[:len(novelXstr3)-1];
  
    
    insertionCols=novelXstr
    insert="insert into DailyTable() Values()"
    query="select*from DailyTable"
    SQLite3conn=sqlite3.connect("DailyDB")
    cursor=SQLite3conn.cursor();
    try:
     cursor.execute(novelXstr2);
     print("Table 'DailyTable' Created"); 
    except:
      print("Table 'DailyTable' already exists");    
        
    rowcount=0;
    while rowcount<len(x):
          littleStr="";       
          littlecount=0;
          while littlecount<len(x.iloc[rowcount]):
                littleStr=littleStr+str(x.iloc[rowcount][littlecount])+","
                littlecount=littlecount+1;
                
          littleStr=littleStr[:len(littleStr)-1]
          insertionOrder="insert into DailyTable("+novelXstr3+") Values("+littleStr+")"
          print(insertionOrder)  
          #print(novelXstr)
          cursor.execute(insertionOrder);
          rowcount=rowcount+1;
    
    cursor.execute(query);
    results=cursor.fetchall();
    results=pandas.DataFrame(results);
    #print(type," -- ",type(results))
    
    
    results.columns=x.columns;
    #print(results.columns);
    print(results);
    NewFrameTitles
    print(len( NewFrameTitles),"  NewFrameTitles - ",NewFrameTitles) 
    print(len(novelXstr)," novelXstr - ",novelXstr)
    print(len(novelXstr2)," novelXstr2 - ",novelXstr2)
    print(len(novelXstr3)," novelXstr3 - ",novelXstr3)
       
    #print("end Make Daily")
    SQLite3conn.close();
    

    
    

