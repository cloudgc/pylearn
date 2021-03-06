import pymysql

host = "cloudfun.org"
use = "root"
pwd = "cloud_Gc3"
usedb = "mysql"

db = pymysql.connect(host, use, pwd, usedb)

cursor = db.cursor()

cursor.execute("select version()")

one = cursor.fetchone()

print(one)

alldata = cursor.fetchall()
print(alldata)

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = "CREATE TABLE EMPLOYEE ( \
         FIRST_NAME  CHAR(20) NOT NULL, \
         LAST_NAME  CHAR(20), \
         AGE INT,  \
         SEX CHAR(1), \
         INCOME FLOAT )"

cursor.execute(sql)

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

db.close()
