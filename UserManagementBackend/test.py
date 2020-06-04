import hashlib
import pymysql
import json

s = 'hello123'
sha = hashlib.sha1()
sha.update(s.encode('utf-8'))
print(sha.hexdigest(),len(sha.hexdigest()))
#
#
# class A:
#     pass
#
#
# a = A()
# print(dir(a))
# print(a.__module__)
# print(a.__class__)
# print(a.__dict__)
#
# db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
#                      passwd='767872313', db='test', charset="utf8")
# cursor = db.cursor()
# sql_string = "show processlist"
# cursor.execute(sql_string)
# results = cursor.fetchall()
# for row in results:
#     print(row)
# cursor.close()  # 关闭游标
# db.close()  # 关闭连接


# data = {
#         'user': 'root',
#         'password': '767872313',
#         'host': '127.0.0.1',
#         'port': 3306,
#         'database': 'test',
#         'encoding': 'utf8',
#         'other': {
#             'author': 'Aileon',
#             'version': 1.0,
#         },
#         }
# with open('config.json', 'w', encoding='utf-8') as f:
#     # indent 格式化保存字典，默认为None，小于0为零个空格
#     # f.write(json.dumps(data, indent=4))
#     json.dump(data, f, indent=4)  # 传入文件描述符，和dumps一样的结果

# with open('config.json', 'r', encoding='utf-8') as f:
#     json_data = json.load(f)
#
# print(json_data['s'])

# print(bin(65535))
# sqlalchemy.exc.IntegrityError   完整性错误，错误码1452是外键列输入的值不存在，错误代码1062是唯一键列的值重复
from UserManagementBackend.UserORM import Session, Users, Auths
s = set()
s.add('root')
s.add('zz')
session = Session()
new_user = Users(name='root', password='123', remote_identity='XX')
session.add(new_user)
session.commit()
session.close()

