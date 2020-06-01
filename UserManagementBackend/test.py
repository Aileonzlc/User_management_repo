import hashlib
import pymysql

s = 'hello123'
sha = hashlib.sha1()
sha.update(s.encode('utf-8'))
print(sha.hexdigest(),len(sha.hexdigest()))


class A:
    pass


a = A()
print(dir(a))
print(a.__module__)
print(a.__class__)
print(a.__dict__)

db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                     passwd='767872313', db='test', charset="utf8")
cursor = db.cursor()
sql_string = "show processlist"
cursor.execute(sql_string)
results = cursor.fetchall()
for row in results:
    print(row)
cursor.close()  # 关闭游标
db.close()  # 关闭连接
