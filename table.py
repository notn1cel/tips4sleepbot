import sqlite3

table = sqlite3.connect("users.db")
cursor = table.cursor()

table.execute("create table users(userid int, day int)")
