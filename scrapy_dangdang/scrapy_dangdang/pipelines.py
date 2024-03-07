# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用管道的话，那么就必须必须在settings中开启管道
class ScrapyDangdangPipeline:
    # 该方法会在爬虫开始的时候调用一次
    def open_spider(self, spider):
        print('===========爬虫开始了==========')
        self.fp = open('book.json','w',encoding='utf-8')


    # item 就是yeild后面的book对象
    def process_item(self, item, spider):
        # 以下这种模式不推荐  因为每传递过来一个对象 就会打开一次文件 这样会导致频繁的IO操作

        # # 1. write方法必须要写一个字符串，而不能是其他的对象
        # # 2. w模式会覆盖之前的内容，a模式会追加内容
        # with open('book.json','a',encoding='utf-8') as f:
        #     f.write(str(item),)
        #     f.write('\n')

        self.fp.write(str(item)+'\n')

        return item

    # 当爬虫结束的时候，这个方法会被调用
    def close_spider(self, spider):
        self.fp.close()
        print('==========爬虫结束了==========')

import urllib.request

# 多条管道同时开启
# 1. 定义管道类
# 2. 在settings中开启管道 "scrapy_dangdang.pipelines.DangDangDownloadPipeline": 301,



class DangDangDownloadPipeline:
    def process_item(self, item, spider):

        url = 'http:'+item.get('img')
        filename = 'D:\\pycharm\\pc_workspace\\爬虫\\当当网图片\\'+item.get('name')+ '.jpg'

        urllib.request.urlretrieve(url=url,filename=filename)

        return item

from scrapy.utils.project import get_project_settings # 加载settings的文件
import pymysql
class MysqlPipline:

    def open_spider(self, spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.dbname = settings['DB_NAME']
        self.port = settings['DB_PORT']
        self.charset = settings['DB_CHARSET']
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.dbname, port=self.port, charset=self.charset)

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        print('正在将数据存入数据库......')
        img_with_http = 'http:'+item.get('img')
        name = item.get('name')
        price = item.get('price')

        sql = 'insert into booksinfo_tb values("{}", "{}", "{}")'.format(name, img_with_http, price)


        # 执行sql语句
        self.cursor.execute(sql)
        self.conn.commit() # 提交事务

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

