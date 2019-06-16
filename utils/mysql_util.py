# -*- coding: UTF-8 -*-
import pymysql


class MySqlUtil:
    def __init__(self, host, user, passwd, db, port=3306):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                                    charset="utf8")

    def mysql_select(self, sql):
        result = ()
        try:
            # 创建游标
            cursor = self.conn.cursor()
            # 执行mysql语句，并返回执行的结果
            rows = cursor.execute(sql)
            if rows > 0:
                result = cursor.fetchall()
        except Exception as e:
            return e
            # 关闭游标
        cursor.close()
        return result

    def mysql_in_up_del(self, sql):
        result = 0
        try:
            cursor = self.conn.cursor()
            rows = cursor.execute(sql)
            if rows > 0:
                result = rows
            # 提交到数据库执行，否则无法保存新建或者修改数据
            self.conn.commit()
        except Exception as e:
            # 回滚数据以防出现错误
            self.conn.rollback()
            return e
        cursor.close()
        return result

    def conn_close(self):
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    # sql_util = MySqlUtil(host="192.168.20.156", user="test_user", passwd="test_user!@#123", db="easyweb_new_trans")
    sql = "select * from W_UserBaseInfo WHERE id = 17519255 "
    sql_util = MySqlUtil(host="127.0.0.1", user="admin", passwd="123456", db="test_db")
    sql_s = "select * from api_user where email='653654@163.com'"
    print("select: ", sql_util.mysql_select(sql_s))
    sql_in = "insert into api_user (id,username,email,groups) values(9,'gfdhgfd','fdsgf@111.com','test')," \
             "(8,'gfdhgfd','fdsgf@111.com','test')"
    print("insert: ", sql_util.mysql_in_up_del(sql_in))
    sql_up = "update api_user set username='test2' where id = 1"
    print("update: ", sql_util.mysql_in_up_del(sql_up))
    sql_del = "delete from api_user where id = 9"
    print("delete: ", sql_util.mysql_in_up_del(sql_del))
    sql_util.conn_close()

# 执行事务
# 事务机制可以确保数据一致性。
#
# 事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
#
# 原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
# 一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
# 隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，
#   并发执行的各个事务之间不能互相干扰。
# 持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。
#   接下来的其他操作或故障不应该对其有任何影响。
# Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
#
# 实例：
# # SQL删除记录语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 向数据库提交
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
# 对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。
#
# commit()方法提交游标的所有更新操作，rollback()方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。
