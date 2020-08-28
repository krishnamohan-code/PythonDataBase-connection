import pymysql
con=pymysql.connect(host="localhost",database="mysql",user='root',password="root")
print(con)
# cursor=con.cursor()
# cursor.execute('create table employees(eid int(5) primary key ,ename varchar(20))')
# print("table created sussessfully")
if con:
    print("connection is ready")
else:
    print("connection failed")
