from pymysql import *


conn=connect("localhost","root","1234","test",3306)
cur=conn.cursor()

# python中只有execute，这个可以执行CRUD所有功能
# count=cur.execute("select * from crl_iou_records")
# print(count)
# result = cur.fetchall()
# for i in result:
#     print(i)

#插入数据
count=cur.execute("insert into test(iou_code) values(%s)"%("'aaa'"))
print(count)
conn.commit()
conn.close()