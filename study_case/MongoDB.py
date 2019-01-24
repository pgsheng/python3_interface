# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/10/23 14:31
"""
import subprocess
import time

import pymongo

from public.log import Log


class MongoDB(object):
    def __init__(self):
        self.log = Log().get_logger()
        """
        1、连接MongoDB
            连接MongoDB我们需要使用PyMongo库里面的MongoClient，一般来说传入MongoDB的IP及端口即可，第一个参数为地址host，
            第二个参数为端口port，端口如果不传默认是27017。
        """
        # self.client = pymongo.MongoClient(host='localhost', port=27017,username='admin',password='pgsheng123')
        self.client = pymongo.MongoClient('mongodb://admin:pgsheng123@localhost:27017/')  # 可以达到同样的连接效果。
        """
        2、指定数据库
            MongoDB分为一个个数据库，需要指定要操作哪个数据库，在这里我以test数据库为例进行说明
            注意: 在 MongoDB 中，如果数据库不存在，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)
                并插入一个文档(记录)，数据库才会真正创建。集合创建同理。
        """
        self.db = self.client.testdb
        # self.db = self.client['testdb']  #　两种方式是等价的。

        """
        2.2、读取 MongoDB 中的所有数据库，并判断指定的数据库是否存在
        """
        dblist = self.client.list_database_names()
        if "testdb" in dblist:
            self.log.info("数据库已存在！")
        else:
            self.log.info("数据库不存在！")

        """
        3、指定集合
            每个数据库又包含了许多集合Collection，也就类似与关系型数据库中的表，下一步需要指定要操作的集合，
        在这里我们指定一个集合名称为students，学生集合。还是和指定数据库类似，指定集合也有两种方式。
        """
        self.collection = self.db.students
        # self.collection = self.db['students']

        collist = self.db.list_collection_names()
        if "students" in collist:  # 判断 sites 集合是否存在
            self.log.info("集合已存在！")
        else:
            self.log.info("集合不存在！")

    def db_insert(self):
        """
        4、插入数据,
            对于students这个Collection，我们新建一条学生数据，以字典的形式表示，
            直接调用collection的insert()方法即可插入数据
        """
        student = {"name": "Google", "alexa": "1", "url": "https://www.google.com"}
        result = self.collection.insert_one(student)
        # 在MongoDB中，每条数据都有一个_id属性来唯一标识，如果没有显式指明_id，MongoDB会自动产生一个ObjectId类型的_id属性。
        self.log.info(result.inserted_id)

        students = [
            {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
            {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
            {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        ]
        results = self.collection.insert_many(students)  # 集合中插入多条数据
        # 输出插入的所有文档对应的 _id 值
        self.log.info(results.inserted_ids)

        # students = [
        #     {"_id": 1, "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
        #     {"_id": 2, "name": "Github", "alexa": "109", "url": "https://www.github.com"}
        # ]
        # results = self.collection.insert_many(students)  # 自己指定 id，插入
        # # 输出插入的所有文档对应的 _id 值
        # self.log.info(results.inserted_ids)

    def db_find(self):
        # results = self.collection.find_one()  # 查询集合中的第一条数据。
        # self.log.info(results)
        #
        for x in self.collection.find():  # 查询集合中的所有数据
            self.log.info(x)

        # find() 方法来查询指定字段的数据，将要返回的字段对应值设置为 1。
        # 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
        # # self.collection.find({}, {"name": 0, "alexa": 1}) 会抛异常
        # value_list = self.collection.find({}, {"_id": 0, "name": 1, "alexa": 1})
        # for x in value_list:
        #     self.log.info(x)
        #
        # self.log.info('-' * 20)
        #
        # # 指定条件查询
        # myquery = {"name": "Facebook"}
        # value_list = self.collection.find(myquery)
        # for x in value_list:
        #     self.log.info(x)
        #
        # self.log.info('-' * 20)
        #
        # # 高级查询,第一个字母 ASCII 值大于 "H" 的数据
        # myquery = {"name": {"$gt": "H"}}
        # value_list = self.collection.find(myquery)
        # for x in value_list:
        #     self.log.info(x)
        #
        # self.log.info('-' * 20)
        #
        # # 使用正则表达式查询,第一个字母为 "F" 的数据
        # myquery = {"name": {"$regex": "^F"}}
        # value_list = self.collection.find(myquery)
        # for x in value_list:
        #     self.log.info(x)
        #
        # self.log.info('-' * 20)
        #
        # # 返回指定条数记录，设置指定条数的记录可以使用 limit() 方法，该方法只接受一个数字参数
        # value_list = self.collection.find().limit(2)
        # for x in value_list:
        #     self.log.info(x)

    def db_update(self):
        value_list = self.collection.find()  # 查询集合中的所有数据
        for x in value_list:
            self.log.info(x)

        # # 将 alexa 字段的值为XXX 的改为 XXX
        # myquery = {"alexa": "103"}
        # newvalues = {"$set": {"alexa": "111"}}
        # result = self.collection.update_one(myquery, newvalues) # 只能修匹配到的第一条记录
        # self.log.info('修改数据结果：%s' % result.modified_count)

        # 将 alexa 字段的值为10000 的改为 111
        myquery = {"alexa": "111"}
        newvalues = {"$set": {"alexa": "112"}}
        result = self.collection.update_many(myquery, newvalues, upsert=True)  # 修改所有匹配到的记录,upsert=True不存在就插入，默认是False
        self.log.info('修改数据结果：%s' % result.modified_count)

        self.log.info('-' * 20)

        value_list = self.collection.find()  # 查询集合中的所有数据
        for x in value_list:
            self.log.info(x)

    def db_sort(self):
        # value_list = self.collection.find().sort("alexa")  # 对字段 alexa 按升序排序
        value_list = self.collection.find().sort("alexa", -1)  # 对字段 alexa 按降序排序
        for x in value_list:
            self.log.info(x)

    def db_delete(self):
        # myquery = {"name": "Taobao"}
        # self.collection.delete_one(myquery)# 删除 name 字段值为 "Taobao" 的第一个匹配文档

        myquery = {"name": {"$regex": "^G"}}
        result = self.collection.delete_many(myquery)  # 删除所有 name 字段中以 G 开头的文档
        self.log.info('删除结果：%s' % result.deleted_count)

        self.db.drop_collection("students") #  删除整个collection

        value_list = self.collection.find()
        for x in value_list:
            self.log.info(x)

        # self.collection.drop() # 删除一个集合
        # collist = self.db.list_collection_names()
        # if "students" in collist:  # 判断 sites 集合是否存在
        #     self.log.info("集合已存在！")
        # else:
        #     self.log.info("集合不存在！")


if __name__ == '__main__':
    m = MongoDB()
    # m.db_insert()
    m.db_find()
    # m.db_update()
    # m.db_sort()
    # m.db_delete()
    client = pymongo.MongoClient('mongodb://admin:pgsheng123@localhost:27017/')
    db = client['scrapydb']  # 指定数据库
    collection = db['teachers']  # 指定集合
    for x in collection.find():  # 查询集合中的所有数据
        print(x)

"""
常见异常：
    1、pymongo.errors.ServerSelectionTimeoutError: localhost:27017: [WinError 10061] 
    由于目标计算机积极拒绝，无法连接。 原因：未装MongoDB或者MongoDB服务没有开启
    2、启动服务：mongod --dbpath E:\MongoDB\data  或 net start MongoDB（管理员打开cmd）
    3、关闭：net stop MongoDB
"""
