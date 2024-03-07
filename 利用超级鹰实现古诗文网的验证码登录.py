import requests
from bs4 import BeautifulSoup
from chaojiying import Chaojiying_Client

# 获取页面的源码
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
}
response = requests.get(url=url,headers=headers)
content = response.text

# 解析页面源码获取__VIEWSTATE和__VIEWSTATEGENERATOR的值
soup = BeautifulSoup(content,'lxml')
__VIEWSTATE_data = soup.find('input',id='__VIEWSTATE')['value']
__VIEWSTATEGENERATOR_data = soup.find('input',id='__VIEWSTATEGENERATOR')['value']

# 获取验证码图片
code = soup.find('img',id='imgCode')['src']
code_url = 'https://so.gushiwen.cn'+code
session = requests.session()
response_code = session.get(code_url)
content_code = response_code.content # 注意此时要使用二进制数据  因为我们要使用的是图片的下载 就不能用text
with open('code.jpg','wb') as fp:
    fp.write(content_code)

# 通过超级鹰识别验证码
chaojiying = Chaojiying_Client('cdutksw', 'Wxw020601.', '957771')  # 用户中心>>软件ID 生成一个替换 96001
im = open(r'D:\pycharm\pc_workspace\爬虫\code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
code_num = chaojiying.PostPic(im, 1902).get('pic_str')
print(f'利用超级鹰识别到的验证码为：{code_num}')

# 点击登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data = {
    '__VIEWSTATE':__VIEWSTATE_data,
    '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR_data,
    'from':'http://so.gushiwen.cn/user/collect.aspx',
    'email':'wxw020601',
    'pwd':'Wxw020601.',
    'code':code_num,
    'denglu':'登录'
}

# 发送post请求
response_post = session.post(url=url_post,headers=headers,data=data)
content_post = response_post.text

# 保存登录后的页面
with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(content_post)