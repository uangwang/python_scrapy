import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    # 入股请求的url是html结尾的那么不需要加/
    start_urls = ["https://car.autohome.com.cn/price/brand-33.html"]

    def parse(self, response):
        print("===================")
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        # for name in name_list:
        #     print(name.extract())
        #     # print(name)
        # print("===================")

        prise_list = response.xpath('//div[@class="main-lever-right"]//span[@class="font-arial"]/text()')
        # for prise in prise_list:
        #     print(prise.extract())
        #     # print(prise)

        for name, prise in zip(name_list, prise_list):
            print(f'车名：{name.extract()} 价格：{prise.extract()}')

