import requests

url = 'http://www.baidu.com'

response = requests.get(url)

# 一个类型和六个属性

# print(type(response)) # <class 'requests.models.Response'>直接是response类型，而urlib是http.client.HTTPResponse

# 六个属性
# 可以设置响应的编码格式
# response.encoding = 'utf-8'
# print(response.text) # 返回的是网页的源代码,以字符串的形式

print(response.url) # 返回的是网页的url
response.encoding = 'utf-8'
# print(response.content) # 返回的是网页的源代码,以字节的形式

print(response.status_code) # 返回的是网页的状态码

print(response.headers) # 返回的是网页的头部信息