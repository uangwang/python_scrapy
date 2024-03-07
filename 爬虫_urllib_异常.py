import urllib.request
import urllib.error
# url = 'https://blog.csdn.net/boysoft2002/article/details/1353959461' # HTTPError

url = 'http://www.goudan11111.com' # URLError

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
}
# 封装data实在post请求或者get请求中涉及变量的时候才使用

try:
    request = urllib.request.Request(url=url,headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)

except urllib.error.HTTPError:
    print('HTTPError')
except urllib.error.URLError:
    print('URLError')