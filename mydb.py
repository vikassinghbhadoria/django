import mysql.connector
database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='191112270',

)
cursorObject=database.cursor()

cursorObject.execute("CREATE DATABASE abc")

print("aal done")