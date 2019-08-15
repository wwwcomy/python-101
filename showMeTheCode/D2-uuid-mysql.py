import uuid
import mysql.connector

#0001
arr=[]
for i in range(0,100):
    # notice there's a comma at the end
    arr.append((str(uuid.uuid1()),))
print(arr)

#pip install mysql-connector-python

#0002
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="",  # 数据库密码
    database="python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO coupon(coupon_txt) VALUES (%s)"

mycursor.executemany(sql,arr)
# mycursor.execute("INSERT INTO coupon(coupon_txt) VALUES (%s)",('bbb',))
mydb.commit()
print(mycursor.rowcount)