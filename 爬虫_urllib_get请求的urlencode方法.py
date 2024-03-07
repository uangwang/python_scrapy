# urlencode应用场景： 多个参数的时候

import urllib.parse
import urllib.request

# https://www.baidu.com/s?wd=周杰伦&sex=男&age=18

# data = {
#     'wd':'周杰伦',
#     'sex':'男',
#     'age':18,
#     'location':'中国台湾'
# }
#
# a = urllib.parse.urlencode(data)
# print(a)

# 获取 https://www.baidu.com/s?wd=周杰伦&sex=男&age=18 的网页源码

base_url = 'https://www.baidu.com/s?'

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾'
}
new_data = urllib.parse.urlencode(data)

url = base_url + new_data

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'Cookie':'BIDUPSID=0B8E9E9E9E9E9E9E9E9E9E9E9E9E9E9E; PSTM=1607525636; BAIDUID=0B8E9E9E9E9E9E9E9E9E9E9E9E9E9E9E:FG=1; BD_UPN=12314753; BDUSS=V5b'
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
