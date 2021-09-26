print("pre import sql")
import sqlite3
SQLite3conn=sqlite3.connect("DB1")
cursor=SQLite3conn.cursor();
cursor.execute("select*from TB1;")
p-cursor.fetchall();
print(cursor)
print(p)
print("post connect")
