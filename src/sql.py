import sqlite3

with sqlite3.connect("users.db") as connections:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users(username TEXT, password TEXT)")
    cursor.execute('INSERT INTO users VALUES("Hello")')