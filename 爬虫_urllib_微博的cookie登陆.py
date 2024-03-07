# 适用场景： 数据采集的时候需要绕过登录然后进入到某个页面进行数据采集
# 个人信息页面是utf-8  但是还报错编码错误  因为并没有进入到个人信息页面 而是跳转到了登陆页面
# 那么登陆页面不是utf-8 所以报错

# 什么情况下访问不成功？
# 因为请求头的信息不够  所以访问不成功

import urllib.request

url = 'https://weibo.com/u/5641941063'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ',
    # cookie中携带者你的登录信息，  如果登录之后的cookie 那么我门就可以携带者cookie去访问个人信息页面
    'Cookie':'SINAGLOBAL=2945669356446.139.1703226416301; XSRF-TOKEN=uTSH1bxN0BxkkvotSV3yjn5B; PC_TOKEN=4c92b7067d; login_sid_t=4e791882edea72a7203e2fc27d18f812; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=7116857115547.515.1705827867938; ULV=1705827867940:2:1:1:7116857115547.515.1705827867938:1703226416302; wb_view_log=1536*8641.25; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFulib6hG6vw3jFTsOWYjN55JpX5o275NHD95QfSoBp1KBpehq0Ws4DqcjNi--ciKyWi-zpi--fi-2EiK.4i--Xi-zRiKn7i--Xi-zRi-8Wi--Xi-iWi-iWi--NiKL2i-2pP7tt; ALF=1708419902; SSOLoginState=1705827902; SUB=_2A25IqK5tDeRhGeNI71MY9C_MzT-IHXVrx6-lrDV8PUNbktAGLVnVkW9NSGY8I4AsAeA1zMYtxxZliTVmtf5jJYY_; WBPSESS=hZ-GNXPMdewda30B22EYwbtwvM5nI7fKb1I9EYnOFB6B083ZfQZWTIEazlDfU39HR-L97lKtIfLNhtO_ei6YXXIVLGe7KVaoB6Bl0y1cpRc7LERxVUdM3lsRY3ex4aDZlKOgkchbCuLGHBSI2vUDyg==',
    # Referer 判断当前路径是不是由上一个路径来的  一般情况下  是做图片防盗链
    'Referer':'https://weibo.cn/'
}
# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)
# 获取响应数据
content = response.read().decode('utf-8')
# 将数据保存
with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)

print(content)