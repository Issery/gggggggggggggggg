import pyodbc
import pandas as pd
import os



# Driver={ODBC Driver 13 for SQL Server};Server=tcp:test1-server.database.windows.net,1433;Database=test1database;Uid=lancer;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
print('ing')
cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:test1-server.database.windows.net;Database=test1database;Uid=lancer;Pwd=Lrd19970323;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
cursor = cnxn.cursor()
print('done!')
# query = 'UPDATE people SET username=?, userstate=?, salary=?, grade=?, room=?, telnum=?, picture=?, keywords=? WHERE username=? \
#   if @@rowcount = 0 \
#   INSERT INTO people VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
#
# for row in data:
#     row = [None if item == 123 else item for item in row]
#     cursor.execute(query, row + [row[0]] + row)
#     cursor.commit()