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
        self.conn = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='123456',
                                    database='teacherdb',  # 数据库不存在话会抛异常
                                    charset='utf8')
        # self.cursor = self.conn.cursor() # 游标默认获取的数据是元祖类型
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 游标设置为字典类型

    def db_create(self):
        self.cursor.execute('SELECT VERSION()')
        data = self.cursor.fetchone()
        self.log.info('Database version:%s' % data)
        # sql = 'CREATE DATABASE IF NOT EXISTS teacherdb DEFAULT CHARACTER SET UTF8'
        # self.cursor.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS teacher (id INT auto_increment PRIMARY KEY ,' \
              'name VARCHAR(10) NOT NULL UNIQUE,age TINYINT NOT NULL)ENGINE=innodb DEFAULT CHARSET=utf8;'
        self.cursor.execute(sql)  # 执行SQL语句
        self.cursor.close()  # 关闭光标对象
        self.conn.close()

    def db_insert(self):
        # 执行SQL，并返回受影响行数,执行多次
        effect_row = self.cursor.executemany("insert into teacher(name,age)values(%s,%s)",
                                             [("小米", 100), ("小红", 101), ("小华", 102)])
        self.log.info('影响行数:%s' % effect_row)
        self.conn.commit()  # 提交，不然无法保存新建或者修改的数据
        self.cursor.close()
        self.conn.close()
        # 获取自增id
        new_id = self.cursor.lastrowid
        self.log.info('自增id:%s' % new_id)

    def db_find(self):
        sql = "select * from teacher;"
        effect_row = self.cursor.execute(sql)
        # fetch数据时按照顺序进行，可以使用cursor.scroll(num, mode)来移动游标位置，如：
        # self.cursor.scroll(1, mode='relative')  # 相对当前位置移动
        # self.cursor.scroll(2, mode='absolute')  # 相对绝对位置移动
        data1 = self.cursor.fetchone()  # 按照顺序进行
        # data2 = self.cursor.fetchmany(2)
        data2 = self.cursor.fetchall()
        self.log.info(data1)
        self.log.info(data2)
        # self.log.info('影响行数:%s' % effect_row)
        self.cursor.close()  # 关闭光标对象
        self.conn.close()

    def db_find2(self):
        name = "小米2"
        age = "100"

        # 1、字符串拼接查询语句
        sql = "select name,age from teacher where name='%s' and age='%s' " % (name, age) # %s的引号要加
        # 执行参数化查询
        self.cursor.execute(sql)
        data1 = self.cursor.fetchone()  # 按照顺序进行
        self.log.info(data1)

        # 2、pymysql提供的参数化查询语句，注意与字符串方式的区别
        self.cursor.execute("select name,age from teacher where name like  '%%%s%%'" % name)
        data2 = self.cursor.fetchone()  # 按照顺序进行
        self.log.info(data2)

        self.cursor.close()
        self.conn.close()

    def db_update(self):
        sql = "update teacher set age = 100 where name = '小米'"
        self.cursor.execute(sql)
        # effect_row = self.cursor.execute("update teacher set age = %s where name = %s", ('110', '小米'))

        sql2 = "update teacher set age = 111 ,name = '小马' where id = 13"
        self.cursor.execute(sql2)

        self.conn.commit()  # 提交，不然无法保存新建或者修改的数据
        self.db_find()
        # self.cursor.close()
        # self.conn.close()

    # 存在就更新，不存在就插入
    def db_update2(self):
        # 1、使用replace语法，表中必须有唯一索引
        sql = "replace into teacher(name,age)values('小米2',100)" # REPLACE时，表中必须有唯一索引
        self.cursor.execute(sql)

        # 2、判断存不存在的那个字段要设置成unique索引,这里前后name值要一样，前面数据是插入，后面是更新
        sql2 = "insert into teacher(name,age)values('小马2',110) on duplicate key update name= '小马2',age=100"
        self.cursor.execute(sql2)

        self.conn.commit()  # 提交，不然无法保存新建或者修改的数据
        self.db_find()
        # self.cursor.close()
        # self.conn.close()

    def db_delete(self):
        sql = "delete from teacher where name = '小米'"
        self.cursor.execute(sql)

        self.conn.commit()  # 提交，不然无法保存新建或者修改的数据
        self.db_find()
        # self.cursor.close()
        # self.conn.close()


if __name__ == '__main__':
    m = MySQLStudy()
    # m.db_create()
    # m.db_insert()
    # m.db_find()
    m.db_find2()
    # m.db_update()
    # m.db_update2()
    # m.db_delete()

"""
123456
启动：mysqld --console 关闭窗口即关闭
      net start mysql 关闭窗口服务还是打开的，关闭方式 net stop mysql
"""
