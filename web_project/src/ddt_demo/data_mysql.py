# -*- coding:utf-8 -*-
import MySQLdb
import pysnooper

# 创建 test_data_db 数据库
creat_database = "CREATE DATABASE IF NOT EXISTS test_data_db DEFAULT CHARSET utf8 COLLATE utf8_general_ci"
# 创建testdate表
creat_table = """
    drop table if exists testdata;
    create table testdata(
        id int not null auto_increment comment "主键",
        bookname varchar(40) unique not null comment "书名",
        author varchar(30) not null comment "作者",
        primary key(id)
        )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 comment "测试数据表"
"""


# ENGINE=InnoDB使用innodb存储引擎
# DEFAULT CHARSET=utf8 数据库默认编码为utf-8
# AUTO_INCREMENT=1 自增键的起始序号为1

class DataBaseInfo:
    def __init__(self, host, port, db, username, password, charset):
        self.db = db
        self.conn = MySQLdb.connect(
            host=host,
            port=port,
            db=db,
            user=username,
            password=password,
            charset=charset)

    def creat(self):
        try:
            # 获取数据库游标
            cursor = self.conn.cursor()
            # 创建数据库
            cursor.execute(creat_database)
            # 选择数据库
            self.conn.select_db(self.db)
            # 创建测试表
            cursor.execute(creat_table)
            self.conn.commit()
        except MySQLdb.Error as e:
            raise e
        else:
            cursor.close()

    def insert_data(self):
        try:
            self.conn.select_db(self.db)
            cursor = self.conn.cursor()
            sql = "insert info test_data(bookname,author) values('时间简史', '斯蒂芬·威廉·霍金'), ('人类简史', '尤瓦尔·赫拉利'), ('未来简史', '尤瓦尔·赫拉利');"
            cursor.execute(sql)
            self.conn.commit()
        except MySQLdb.Error as e:
            raise e
        else:
            cursor.close()

    def get_data(self):
        self.conn.select_db(self.db)
        cursor = self.conn.cursor()
        sql = "select * from test_data;"
        cursor.execute(sql)
        data_tupl = cursor.fetchall()
        self.conn.commit()
        cursor.close()
        return data_tupl

    def close_conn(self):
        self.conn.close()


if __name__ == '__main__':
    db = DataBaseInfo(host="127.0.0.1",
                      port=3306,
                      db="test_data_db",
                      username="admin",
                      password="123456",
                      charset="utf8mb4")
    db.insert_data()
    db.close_conn()
