# -*- coding: UTF-8 -*-
import pymysql


class MySqlUtil:
    def __init__(self ):
        self.conn = pymysql.connect(host="192.168.20.156", port=3306, user="test_user", passwd="test_user!@#123",
                 db="easyweb_new_trans")

    def mysql_select(self, sql):
        cursor = self.conn.cursor()
        # 执行mysql语句，并返回执行的结果
        rows = cursor.execute(sql)
        if rows == 1:
            result = cursor.fetchall()
        else:
            result = ""
        # 把要执行的语句提交，否则无法保存新建或者修改数据
        self.conn.commit()
        # 关闭游标
        self.cursor.close()
        print(result)
        return result

    def mysql_insert_one(self):
        cursor = self.conn.cursor()
        rows = cursor.execute(sql)
        if rows == 1:
            result = 1
        else:
            result = 0
        self.conn.commit()
        self.cursor.close()
        return result


    def conn_close(self):
        # 关闭连接
        self.conn.close()


if __name__ == '__main__':
    sql_util = MySqlUtil()
    sql = "select * from W_UserBaseInfo WHERE id = 17519255 "
    sql_util.mysql_select(sql)
    sql_util.conn_close()