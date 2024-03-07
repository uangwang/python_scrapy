# 通过登录  然后进入到主页面
import urllib

# 通过找登录接口发现  登录的时候需要的参数很多
# __VIEWSTATE: gS58p8PrY1spodiijo9XZkE/NUfi/UGKDj+NG1BVJ6Voc46JuAj/3CLRzk14kf0mhx8a3Aci7MVCUuvmly65VDCy+YQq7ieJbOxhEXeC5XZ0bIlKEWehKjPl2Xu4qejTwZlzbNlrtTQhjD/0j6MDW4d1SzM=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: cdutksw@163.com
# pwd: Wxw020601.
# code: EYRU
# denglu: 登录

# 观察到_ViewState和_ViewStateGenerator是动态变化的，是变量

# 难点1：_ViewState和_ViewStateGenerator  一般情况下看不到的数据都在页面的源码中
#  通过查看源码发现这两个数据在页面的源码中，所以我们需要获取页面的源码，然后进行解析就可以获取了
# 难点2：验证码

import requests

# 登录页面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
}
# 获取页面的源码
response = requests.get(url=url,headers=headers)
content = response.text
# print(content)

# 解析页面源码获取__VIEWSTATE和__VIEWSTATEGENERATOR的值
from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')
# 获取__VIEWSTATE和__VIEWSTATEGENERATOR的值
__VIEWSTATE_data = soup.find('input',id='__VIEWSTATE')['value']
__VIEWSTATEGENERATOR_data = soup.find('input',id='__VIEWSTATEGENERATOR')['value']
# print(__VIEWSTATE_data)
# print(__VIEWSTATEGENERATOR_data)

# 获取验证码图片
code = soup.find('img',id='imgCode')['src']
code_url = 'https://so.gushiwen.cn'+code

# requests里面有个方法 session() 通过session的返回值 就能使用请求变成一个对象

session = requests.session()
response_code = session.get(code_url)
# 注意此时要使用二进制数据  因为我们要使用的是图片的下载 就不能用text
content_code = response_code.content
# wb的模式是将二进制写入到文
with open('code.jpg','wb') as fp:
    fp.write(content_code)

# downcodeimg = urllib.request.urlretrieve(code_url,'code.jpg') #错误，再次请求的时候 验证码其实已经变了

# #提取图片中的数字字母
# from PIL import Image
# import pytesseract
# from io import BytesIO
# new_img = Image.open('code.png')
# # 识别验证码
# pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\Tesseract-OCR\tesseract.exe'
# code_text = pytesseract.image_to_string(new_img)
# print(code_text)


# # 通过验证码图片获取验证码
# from PIL import Image
# import pytesseract
# from io import BytesIO
#
# # 下载验证码图片
# response_codeurl = requests.get(code_url)
# img = Image.open(BytesIO(response_codeurl.content))
#
# # 使用 pytesseract 进行验证码识别
# captcha_text = pytesseract.image_to_string(img)
#
# print("识别到的验证码:", captcha_text)

from chaojiying import Chaojiying_Client
# 利用超级鹰方法识别验证码
chaojiying = Chaojiying_Client('cdutksw', 'Wxw020601.', '957771')  # 用户中心>>软件ID 生成一个替换 96001
im = open(r'D:\pycharm\pc_workspace\爬虫\code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
code_name = chaojiying.PostPic(im, 1902).get('pic_str')
print(f'利用超级鹰识别到的验证码为：{code_name}')
# code_name = input('请输入验证码：')

# 点击登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post = {
    '__VIEWSTATE':__VIEWSTATE_data,
    '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR_data,
    'from':'http://so.gushiwen.cn/user/collect.aspx',
    'email':'cdutksw@163.com',
    'pwd':'Wxw020601.',
    'code':code_name,
    'denglu':'登录'
}

response_post = session.post(url=url_post,headers=headers,data=data_post)
content_post = response_post.text

with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(content_post)

# 难点
# 1.隐藏域
# 2.验证码