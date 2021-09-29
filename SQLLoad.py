print("pre import sql")
import sqlite3
import pandas
#import datetime
from datetime import date

print(date.today())



def CallFromSQL(x,y,date):
    date=str(date);
    #date2=str(date2);
    SQLite3conn=sqlite3.connect("DailyDB");
    query="select*from DailyTable"
    query.replace("*",x).replace("DailyTable",y)
    #if date.find("-")>-1:
       #query=query+" where insertionDay = '"+date+"';"  
    cursor=SQLite3conn.cursor();
    #print(query)    
    cursor.execute(query);
    info=cursor.description;
    info=pandas.DataFrame(info);
    titles=info[0]
    
    results=cursor.fetchall();
    results=pandas.DataFrame(results);
    #print(query);
    print(titles);
    #print(results);
    #print(len(results));
    results.columns=titles;
    #results=results.to_html()
    #print(results);
    cursor.close();
    #print(" end CallFromSQL()")
    return results;

def MakeDailyTable(z,a):
    """
    SQLite3conn=sqlite3.connect("DailyDB")
    cursor=SQLite3conn.cursor();
    cursor.execute("drop table DailyTable;")
    SQLite3conn.commit()
    SQLite3conn.close()
    #SQLite3conn.commit()
    """
    
    tablename="DailyTable";
    
    print("start of makeDailyTable ")
    a='"'+a+'"';
    curDate='"'+str(date.today())+'"'
    CurrentDate=[];
    symbolCol=[];
    for symb in z['index']:
        symbolCol.append(a);
        CurrentDate.append(curDate);
    z[['Symbol']]=symbolCol;
    z[['insertionDay']]=CurrentDate;
          
    x=z.drop(columns=['index','date'])
    NewdateCol1=[];
    acount=0;
    while acount<len(z['date']):
          NewDateEntry='"'+z['date'][acount]+'"';
          NewdateCol1.append(NewDateEntry)  
          acount=acount+1;
    x['date']=NewdateCol1;        
    print("date rectification")    
    
    
    
    
    novelXstr="";
    y=x.columns;
    for elem in y:
        strtest=str(type(x[elem][1]))+str(type(x[elem][2]))+str(type(x[elem][3]))+str(type(x[elem][4]))+str(type(x[elem][5]));
        if strtest.find('str')>-1:
           elem="'"+elem+"'"+" TEXT, ";
        else:
           elem="'"+elem+"'"+" REAL, ";
        novelXstr=novelXstr+elem;
    novelXstr=novelXstr[:len(novelXstr)-1];
    novelXstr2="create table DailyTable("+novelXstr[:len(novelXstr)-1]+");"
    novelXstr2=novelXstr2.replace("DailyTable",tablename)
    novelXstr3=novelXstr.replace(" REAL","");
    novelXstr3=novelXstr3.replace(" TEXT","");
    novelXstr3=novelXstr3.replace(" BLOB","");
    novelXstr3=novelXstr3[:len(novelXstr3)-1];
    print("Data Type Rectification ")
  
    print("Begining Table making")
    insertionCols=novelXstr
    insert="insert into DailyTable() Values()"
    insert.replace("DailyTable",tablename)
    #query="select*from DailyTable"
    
    SQLite3conn=sqlite3.connect("DailyDB")
    cursor=SQLite3conn.cursor();
    #cursor.execute(novelXstr2);
    try:
     print("Try Trying 1") 
     print(novelXstr2)
     print("Try Trying 1.5")    
     cursor.execute(novelXstr2);
     print("Try Trying 2")    
     rmess="Table 'DailyTable' Created"
     print("Try Trying 3")       
     rmess.replace("DailyTable",tablename) 
     print("Try Trying 4")       
     print(rmess); 
     print("Try Trying 5")       
    except:
     rmess="Tried to create Table failed ssuming Table 'DailyTable' already exists"
     rmess.replace("DailyTable",tablename)  
     print(rmess);    
    cursor.close()    
    print("Beginging Table insertion")
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
          #SQLite3conn.commit()
          rowcount=rowcount+1;
    
    """
    SQLite3conn=sqlite3.connect("DailyDB")
    cursor=SQLite3conn.cursor(); 
    cursor.execute(novelXstr2);
    SQLite3conn.commit() 
    SQLite3conn.close();
    """
    print("end Table insertion");
    return;
    #CallFromSQL();  
    
    
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

    
    

