import scrapy
from scrapy_movie.items import ScrapyMovieItem


class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["dy2018.com"]
    start_urls = ["https://dy2018.com/1/"]

    def parse(self, response):
        # 要第一个名字和第二页照片
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            # 获取第一页的name和要点击的url
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = 'https://dy2018.com' + href
            # print(name, url)

            # 对第二页的连接发起访问
            yield scrapy.Request(url, callback=self.parse_second,meta={'name':name})

    def parse_second(self, response):
        # 获取第二页的图片
        img = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # 接收到请求的那个meta参数的值
        name = response.meta['name']

        movie = ScrapyMovieItem(img=img, name=name)

        yield movie