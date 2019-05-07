# -*- coding: UTF-8 -*-
import pymysql


##链接mysql
def select(userid):
    # 创建连接
    conn = pymysql.connect(host="192.168.20.156", port=3306, user="test_user", passwd="test_user!@#123",
                           db="easyweb_new_trans")
    # 创建游标
    cursor = conn.cursor()
    # 执行mysql语句，并返回执行的结果
    sql = "select * from W_UserBaseInfo WHERE userid = %s " % userid
    res = cursor.execute(sql)
    if res == 1:
        for i in cursor.fetchall():
            print(i)
    else:
        print("查询结果为空")
    # 把要执行的语句提交，否则无法保存新建或者修改数据
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
