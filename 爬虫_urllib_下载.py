import urllib.request

# 下载一个网页
# url_page = 'http://www.baidu.com'
# url代表的是下载的路径  filename文件的名字
# 在python中 可以变量的名字 也可以直接写值
# urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载一个图片
# url_imge = 'https://img2.baidu.com/it/u=1306686674,3703984214&fm=253&fmt=auto&app=138&f=JPEG?w=668&h=500'
# urllib.request.urlretrieve(url_imge, 'kun.jpg')

# 下载一个视频
url_video = 'https://vd4.bdstatic.com/mda-pf2haa6erdsb2n0c/sc/cae_h264/1685869711978490981/mda-pf2haa6erdsb2n0c.mp4?v_from_s=hkapp-haokan-hnb&auth_key=1705394576-0-0-5493af48548e4a5ed76a5383f5ea2abf&bcevod_channel=searchbox_feed&pd=1&cr=2&cd=0&pt=3&logid=2576070267&vid=1942850554410227762&klogid=2576070267&abtest='
urllib.request.urlretrieve(url_video, 'kun.mp4')# 视频后缀一般是mp4