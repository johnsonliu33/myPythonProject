# -*- coding:utf-8 -*-

from pymysql import connect
import yaml


class MysqlDB():
    def __init__(self):
        """连接数据库"""
        self.conn = connect(host="127.0.0.1", port=3306, user="admin", password="123456", db="test_db")

    def clear(self, table_name):
        """清除表数据"""
        clear_sql = "truncate " + table_name + ";"
        with self.conn.cursor() as cursor:
            # 清除外键约束
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(clear_sql)
        self.conn.commit()

    def insert(self, table_name, table_data):
        """插入数据"""
        # 遍历数据
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"  # sql语句中的value值需要加引号
        key = ",".join(table_data.keys())
        value = ",".join(table_data.values())
        insert_sql = "insert into " + table_name + "(" + key + ")" + "values" + "(" + value + ")"
        with self.conn.cursor() as cursor:
            count = cursor.execute(insert_sql)
            print("==============", count)
        self.conn.commit()

    def close(self):
        """关闭数据库"""
        self.conn.close()

    def init_data(self, datas):
        """初始化数据"""
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    db = MysqlDB()
    db.clear("api_user")
    db.clear("api_group")
    user_data = {"id": 1, "username": "333nhvgccf", "email": "653654@163.com"}
    db.insert("api_user", user_data)
    group_data = {"id": 1, "name": "333hgfdhtyhy"}
    db.insert("api_group", group_data)
    db.close()
