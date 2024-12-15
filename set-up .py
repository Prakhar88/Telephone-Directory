import mysql.connector as sql 
mydb=sql.connect(host="localhost",username="root",password="Prakhar1",database="Backstreet_Boyz")
cursor=mydb.cursor()
query="set autocommit=1"
cursor.execute(query)
q1="Create Table Directory(ID int(5) Primary key Not null,Name varchar(20) Not null,Address varchar(60) Not null,PriPhone bigint(11) Not null,SecPhone bigint(11))"
cursor.execute(q1)