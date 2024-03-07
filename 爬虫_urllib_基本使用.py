# 使用urllib获取网页源码
import urllib.request


# 1.定义一个url  就是你要访问的地址
url = "http://www.baidu.com"

# 2.模拟浏览器像服务器发送请求  response响应
response = urllib.request.urlopen(url)

# 3.读取响应中的页面的源码
# read方法 返回的是字节形式的二进制数据
# 我们要将二进制的数据转换为字符串
# 二进制----》字符串： 解码   decode（‘编码的格式’）
content = response.read().decode('utf-8')

# 4.打印源码
print(content)