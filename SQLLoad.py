print("pre import sql")
import sqlite3
import pandas
from datetime import date

print(date.today())



def CallFromSQL(x,y,date):
    date=str(date);
    SQLite3conn=sqlite3.connect("DailyDB");
    query='select * from DailyTable'
    if date.find("-")>-1:
       query=query+" where Symbol = '"+x+"' and insertionDay = '"+date+"';"  
    cursor=SQLite3conn.cursor();
    cursor.execute(query);
    info=cursor.description;
    info=pandas.DataFrame(info);
    titles=info[0]
    
    results=cursor.fetchall();
    results=pandas.DataFrame(results);
    if len(results)>0:
        results.columns=titles;
    cursor.close();
    return results;

def MakeDailyTable(z,a):
    listColnames=z.columns;
    FrstCol=listColnames[0];
    print("FrstCol = ",FrstCol);
    ColStr1="";
    for title in listColnames:
        ColStr1=ColStr1+title;
    
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
    for symb in z[FrstCol]:
    #for symb in z['index']:
        symbolCol.append(a);
        CurrentDate.append(curDate);
    z[['Symbol']]=symbolCol;
    z[['insertionDay']]=CurrentDate;
    
    if ColStr1.find('index')>-1:
       x=z.drop(columns=['index']);
    
    if ColStr1.find('date')>-1:
        x=z.drop(columns=['date']);
    #x=z.drop(columns=['index','date'])
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
        #print("x - ",x);
        #print("elem - ",elem)
        strtest=str(type(x[elem][1]))+str(type(x[elem][2]))+str(type(x[elem][3]))+str(type(x[elem][4]))+str(type(x[elem][5]));
        #print("strtest ",strtest)
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
    SQLite3conn=sqlite3.connect("DailyDB")
    cursor=SQLite3conn.cursor();
    try:
     print("Try Trying 1") 
     #print(novelXstr2)
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
     rmess="Tried to create Table failed assuming Table 'DailyTable' already exists"
     rmess.replace("DailyTable",tablename)  
     print(rmess);    
    cursor.close()    
    print("Begining Table insertion")
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
 
    return;
    
    
    

