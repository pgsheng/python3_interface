import pymssql


class MSSQL(object):
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd,
                                    database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        # row = cur.fetchone()
        # while row:
        #     print("ID=%d" % row[0])
        #     row = cur.fetchone()
        # 也可以使用for循环来迭代查询结果
        # for row in cur:
        #     print("ID=%d" % row[0])

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        # 如果 update/delete/insert 记得要 conn.commit() ，否则数据库事务无法提交
        self.conn.commit()
        self.conn.close()


ms = MSSQL(host="192.168.1.1", user="sa", pwd="sa", db="testdb")
reslist = ms.ExecQuery("select * from webuser")
for i in reslist:
    print(i)

newsql = "update webuser set name='%s' where id=1" % u'测试'
print(newsql)
ms.ExecNonQuery(newsql.encode('utf-8'))
