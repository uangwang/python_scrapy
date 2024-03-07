import scrapy
from scrapy_dangdang.items import ScrapyDangdangItem # 报错不用管


class DangSpider(scrapy.Spider):
    name = "dang"
    # 如果是多页下载的话，那么必须要调整allowed_domains的范围，一般情况下只写域名
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.01.02.00.00.00.html"]

    base_url = 'https://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        # pipeline 下载数据
        # items 定义数据结构

        # src('//ul[@id="component_59"]/li//img/@data-original')
        # name('//ul[@id="component_59"]/li//img/@alt')
        # price('//ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()')
        # 所有的Selector的对象 都可以再次调用xpath方法

        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            # 第一张图片和其他的图片的标签的属性是不一样的
            # 第一张图片的src是可以使用的  其他的图片的src是data-original
            img = li.xpath('.//img/@data-original').extract_first()  # 注意这个.//表示当前节点下的img
            if img is None:
                img = li.xpath('.//img/@src').extract_first()
            else:
                img = img
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            # print(img, name, price)

            book = ScrapyDangdangItem(img = img, name = name, price = price)
            # 获取一个book就将book交给pipeline
            yield book

        # 每一页爬取的数据都是一样的 所以我们只需要将执行的那个页码的请求再次调用parse方法
        #https://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
        if self.page <= 2:
            self.page += 1
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'

            # 怎么去调用parse方法
            # scrapy.Request是scrapy的get请求
            # url是请求的url，callback是请求成功之后的回调函数，注意不允许加括号
            yield scrapy.Request(url=url,callback=self.parse)
