print("pre import sql")
import sqlite3
import pandas
#SQLcolsnames="select names from PRAGMA_TABLE_INFO('TB11')"
#SQLcolsnames="PRAGMA"
SQLite3conn=sqlite3.connect("TB1")
cursor=SQLite3conn.cursor();
#a=cursor.execute(SQLcolsnames)
b=cursor.execute("select*from TB11 limit 1;")
c=ColNames=pandas.DataFrame(cursor.description)
c=c[[0]];

#p=cursor.fetchall();

print(cursor)
#print(cursor.description)
#print(SQLcolsnames)
#print(a)
print(b)
print(c)
print("post connect")
