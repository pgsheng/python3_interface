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
                                  database='teacherdb',  # 数据库不存在话会抛异常
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def db_create(self):
        self.cursor.execute('SELECT VERSION()')
        data = self.cursor.fetchone()
        self.log.info('Database version:%s'%data)
        # sql = 'CREATE DATABASE IF NOT EXISTS teacherdb DEFAULT CHARACTER SET UTF8'
        # self.cursor.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS teacher (id INT auto_increment PRIMARY KEY ,' \
              'name VARCHAR(10) NOT NULL UNIQUE,age TINYINT NOT NULL)ENGINE=innodb DEFAULT CHARSET=utf8;'
        self.cursor.execute(sql)  # 执行SQL语句
        self.cursor.close()  # 关闭光标对象
        self.db.close()

    def db_insert(self):
        pass

    def db_find(self):
        sql = "select * from user1;"
        effect_row = self.cursor.execute(sql)
        data1 = self.cursor.fetchone()
        self.log.info(data1)
        self.log.info('影响行数:%s'% effect_row)

    def db_update(self):
        pass

    def db_sort(self):
        pass

    def db_delete(self):
        pass


if __name__ == '__main__':
    m = MySQLStudy()
    # m.db_create()
    m.db_find()

"""
123456
启动：mysqld --console 关闭窗口即关闭
      net start mysql 关闭窗口服务还是打开的，关闭方式 net stop mysql
"""
