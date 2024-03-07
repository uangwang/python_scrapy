# get请求
# 获取豆瓣电影的第一页数据，并且保存起来

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求,获取响应的内容
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

# 数据下载到本地   open方法默认是以gbk的编码打开的，因为有中文所以会报错，所以需要指定编码utf-8
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)

with open('豆瓣/douban2.json', 'w', encoding='utf-8') as fp:
    fp.write(content)