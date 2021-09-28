print("pre import sql")
import sqlite3
import pandas
#import datetime
from datetime import date

print(date.today())



def CallFromSQL():
    print(" start CallFromSQL()")
    SQLite3conn=sqlite3.connect("DailyDB");
    query="select*from DailyTable"
    cursor=SQLite3conn.cursor();
        
    cursor.execute(query);
    info=cursor.description;
    info=pandas.DataFrame(info);
    titles=info[0]
    
    results=cursor.fetchall();
    results=pandas.DataFrame(results);
    
    results.columns=titles;
    #results=results.to_html()
    print(results);
    cursor.close();
    print(" end CallFromSQL()")
    return results;

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
    
    
        
    
    x=z.drop(columns=['index','date'])
    NewdateCol1=[];
    acount=0;
    while acount<len(z['date']):
          NewDateEntry='"'+z['date'][acount]+'"';
          NewdateCol1.append(NewDateEntry)  
          acount=acount+1;
    x['date']=NewdateCol1;        
        
    
    
    
    
    novelXstr="";
    y=x.columns;
    #print("Make Data Input")
    #NewFrameTitles=[];
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
    #query="select*from DailyTable"
    
    SQLite3conn=sqlite3.connect("DailyDB")
    cursor=SQLite3conn.cursor();
    try:
     cursor.execute(novelXstr2);
     print("Table 'DailyTable' Created"); 
    except:
      print("Table 'DailyTable' already exists");    
    cursor.close()    
    
    rowcount=0;
    while rowcount<len(x):
          littleStr="";       
          littlecount=0;
          while littlecount<len(x.iloc[rowcount]):
                ent=x.iloc[rowcount][littlecount]
                littleStr=littleStr+str(x.iloc[rowcount][littlecount])+","
                littlecount=littlecount+1;
                
          littleStr=littleStr[:len(littleStr)-1]
          insertionOrder="insert into DailyTable("+novelXstr3+") Values("+littleStr+")"
          SQLite3conn=sqlite3.connect("DailyDB")
          cursor=SQLite3conn.cursor(); 
          cursor.execute(insertionOrder);
          SQLite3conn.commit() 
          SQLite3conn.close();
          rowcount=rowcount+1;
    CallFromSQL();  
    
    
    #cursor.execute(query);
    #info=cursor.description;
    #info=pandas.DataFrame(info);
    #titles=info[0]
    #print("len -",len(titles)," ",type(titles),"-titles-",titles)
    
    #results=cursor.fetchall();
    #results=pandas.DataFrame(results);
    #print(type," -- ",type(results))
    
    
    #results.columns=titles;
    #results.columns=x.columns;
    #print(results.columns);
    #results=results.to_html()
    #print(results);
    #NewFrameTitles
    #print(len( NewFrameTitles),"  NewFrameTitles - ",NewFrameTitles) 
    #print(len(novelXstr)," novelXstr - ",novelXstr)
    #print(len(novelXstr2)," novelXstr2 - ",novelXstr2)
    #print(len(novelXstr3)," novelXstr3 - ",novelXstr3)
      
    #print("end Make Daily")
    #SQLite3conn.close();
    #CallFromSQL();
    #return results;

    
    

