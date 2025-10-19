import mysql.connector 

mydb = mysql.connector .connect (
    host = "localhost",
    user = "root",
    password = "@Fromh3v3n",
    database = "alx_book_store"
)

if mydb.is_connected():
    print(f"Database '{mydb.database}' created successfully!")