import sqlite3

with sqlite3.connect("users.db") as connections:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users(username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL)")

with sqlite3.connect("runs.db") as connections:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE runs(username TEXT REFERENCES users(username), time TIME, distance INT")
