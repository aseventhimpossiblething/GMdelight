print("pre import sql")
import sqlite3
SQLite3conn=sqlite3.connect("BD1")
cursor=SQLite3conn.cursor();
p=cursor.execute("select*from TB1;")
print(cursor)
print(p)
print("post connect")
