print("pre import sql")
import sqlite3
import pandas
#SQLcolsnames="select names from PRAGMA_TABLE_INFO('TB11')"
#SQLcolsnames="PRAGMA"
SQLite3conn=sqlite3.connect("TB1")
cursor=SQLite3conn.cursor();
#a=cursor.execute(SQLcolsnames)
b=cursor.execute("select*from TB11;")
ColNames=pandas.Dataframe(cursor.description)

#p=cursor.fetchall();

print(cursor)
print(cursor.description)
#print(SQLcolsnames)
#print(a)
print(b)
print("post connect")
