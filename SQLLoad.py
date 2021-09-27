print("pre import sql")
import sqlite3
import pandas



def addToTable(x):
    SQLite3conn=sqlite3.connect("DailyDB");
    cursor=SQLite3conn.cursor();
    cursor.execute();
    

def MakeDailyTable(x,a):
    x=x.drop(columns=['index'])
    novelXstr="";
    y=x.columns;
    print("Make Data Input")
    digcounter=0;
    for elem in y:
        while digcounter<3:
              dig=x[elem][digcounter];
              print(dig,"-",dig,"! - !",type(dig));  
              digcounter=digcounter+1;
        print(elem,"! - !",type(elem))
        
        #if type(elem)==
        elem=elem+" REAL, ";
        novelXstr=novelXstr+elem;
    novelXstr=novelXstr[:len(novelXstr)-1];
    
    novelXstr2="create table DailyTable("+novelXstr[:len(novelXstr)-1]+");" 
    novelXstr3=novelXstr.replace(" REAL","");
    novelXstr3=novelXstr3[:len(novelXstr3)-1];
    #novelXstr4="insert into DailyTable("+novelXstr3+") Values("+littleStr+")"
    
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
                #print(littleStr)
          littleStr=littleStr[:len(littleStr)-1]
          insertionOrder="insert into DailyTable("+novelXstr3+") Values("+littleStr+")"  
          cursor.execute(insertionOrder);
          #print(x.iloc[rowcount])
          rowcount=rowcount+1;
    
    
    
    #cursor.execute(novelXstr2);
    cursor.execute(query);
    results=cursor.fetchall();
    print("results",results)
    #print(x)
    print("novelXstr",novelXstr)
    print("novelXstr2",novelXstr2)
    print("novelXstr3",novelXstr3)
   
    
    print("end Make Daily")
    SQLite3conn.close();
    

    
    

