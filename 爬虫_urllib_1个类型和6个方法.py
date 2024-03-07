import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和6个方法
# print(type(response)) #<class 'http.client.HTTPResponse'>这个类型

# 按照一个字节一个字节的读取
# content = response.read().decode('utf-8')
# print(type(content)) #<class 'str'>

# read里面的数字代表返回多少个字节
# content = response.read(5).decode('utf-8') # 5代表读取5个字节
# print(content)

# readline() 读取一行
# content = response.readline().decode('utf-8') #读取一行
# print(content)

# content = response.readlines(3) #读取多行
# print(content)

# 返回状态码 如果是200 那么就证明我们的逻辑没有错
print(response.getcode()) #获取状态码

# 返回实际数据的url地址
print(response.geturl()) #获取url

# 返回响应头信息
print(response.getheaders()) #获取响应头

# 一个类型：HTTPResponse
# 6个方法：read() readline() readlines() getcode() geturl() getheaders()