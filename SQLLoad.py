print("pre import sql")
import sqlite3
SQLite3conn=sqlite3.connect("BD1")
cursor=SQLite3conn.cursor();
print(cursor)
print("post connect")
