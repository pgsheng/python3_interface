# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/10/23 14:31
"""
import pymysql

from public.log import Log


class MySQLStudy(object):
    def __init__(self):
        self.log = Log().get_logger()
        # 打开数据库连接
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def db_create(self):
        self.cursor.execute('SELECT VERSION()')
        data = self.cursor.fetchone()
        print('Database version:', data)
        self.cursor.execute("CREATE DATABASE teacherdb DEFAULT CHARACTER SET utf8")
        self.db.close()

    def db_insert(self):
        pass

    def db_find(self):
        pass

    def db_update(self):
        pass

    def db_sort(self):
        pass

    def db_delete(self):
        pass


if __name__ == '__main__':
    m = MySQLStudy()
    m.db_create()

"""
123456
启动：mysqld --console 关闭窗口即关闭
      net start mysql 关闭窗口服务还是打开的，关闭方式 net stop mysql

"""
