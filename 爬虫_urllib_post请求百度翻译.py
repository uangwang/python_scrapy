
# post请求
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
keyword = input('请输入要翻译的内容：')
data = {
    'kw':keyword
}

# post的请求的参数必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8') # encode()编码
# post的请求的参数 是不会拼接在url后面的  而是需要放在请求对象定制的参数之中
# post请求的参数必须要进行编码
request = urllib.request.Request(url=url,headers=headers,data=data)

response = urllib.request.urlopen(request)
content = json.loads(response.read().decode('utf-8'))
print(response)
print(content)
print(type(content))