#!/usr/bin/python
import sqlite3
import datetime

conn = sqlite3.connect("database.sqlite")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * from OrderHeaders")
orders = cursor.fetchall()
for order in orders:
    as_int = order['OrderDateTime']
    d = datetime.datetime.fromtimestamp(int(as_int / 1000.)) # FIXME: Time zone?
    print d

