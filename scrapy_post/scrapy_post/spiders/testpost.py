import scrapy
import json

class TestpostSpider(scrapy.Spider):
    name = "testpost"
    allowed_domains = ["fanyi.baidu.com"]
    # post请求  如果没有参数 那么这个请求将没有任何的意义 所以这个start——urls是没有用的
    # 所以parse方法也是没有用的
    # start_urls = ["https://fanyi.baidu.com/sug"]
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        # post请求的url
        url = 'https://fanyi.baidu.com/sug'
        # post请求的参数
        data = {
            'kw':'final'
        }
        # 发送post请求
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)


    def parse_second(self, response):
        obj = json.loads(response.text)
        print(obj)