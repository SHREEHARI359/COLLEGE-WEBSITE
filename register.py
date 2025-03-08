#!C:\Python312\python.exe

import cgi
import mysql.connector
print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body>")


print("<h1> Thanq for register<h1>")


form=cgi.FieldStorage()
fname=form.getvalue("name")
ffname=form.getvalue("fname")
fage=form.getvalue("age")

print("<h1>",fname,ffname,fage,"</h1>")
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SVHEC"
)

mycursor=mydb.cursor()
sql="INSERT INTO student(Name,FName,Age)values(%s,%s,%s)"
value=(fname,fname,fage)
mycursor.execute(sql,value)
mydb.commit()


print("</body>")
print("</html>")