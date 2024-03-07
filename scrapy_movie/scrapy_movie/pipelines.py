# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from scrapy.utils.project import get_project_settings


class ScrapyMoviePipeline:

    def open_spider(self, spider):




        print('开始爬取')
        self.fp = open('movie.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item) + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('爬取完成')
        print('数据已经保存到movie.json文件中')

class MovieDownloadPipeline:
    def open_spider(self, spider):
        print('连接数据库')
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
        sql = 'insert into movie_tb values(img,name) values("{}", "{}")'.format(item.get('img'), item.get('name'))
        self.cursor.execute(sql)
        self.conn.commit() # 提交事务
        return item

    def close_spider(self, spider):
        print('数据存入数据库完成')
        self.cursor.close()
        self.conn.close()
        print('数据库连接已关闭')