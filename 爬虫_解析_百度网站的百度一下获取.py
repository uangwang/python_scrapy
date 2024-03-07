
# 1.获取网页的源码
# 2.解析  解析的服务器的响应的文件  etree.HTML('服务器响应的数据')
# 3.打印

import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器访问服务器
response = urllib.request.urlopen(request)

# 获取响应信息
content = response.read().decode('utf-8')

# 解析网页源码  来获取想要的数据
from lxml import etree
tree = etree.HTML(content)

# 获取数据
result = tree.xpath('//input[@id="su"]/@value')[0]
print(result)