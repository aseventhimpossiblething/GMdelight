print("pre import sql")
import sqlite3
SQLite3conn=sqlite3.connect("DB1")
cursor=SQLite3conn.cursor();
p=cursor.execute(".database;")
print(cursor)
print(p)
print("post connect")
