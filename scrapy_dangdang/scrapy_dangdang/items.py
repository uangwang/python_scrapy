# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 通俗的说就是你要下载的数据都有什么

    # 书籍图片
    img = scrapy.Field()
    # 书籍名称
    name = scrapy.Field()
    # 书籍价格
    price = scrapy.Field()

