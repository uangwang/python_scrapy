
# 1.请求对象的定制
# 2.获取网页的源码
# 3.下载

url = 'https://sc.chinaz.com/tupian/meishitupian.html' #https://sc.chinaz.com/tupian/meishitupian_3.html
# 需求：下载前十页的图片

import urllib.request

def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/meishitupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/meishitupian_{}.html'.format(page)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    }

    request = urllib.request.Request(url=url,headers=headers)
    return request
    print(url)

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download_content(content):
    # 下载图片
    # urlib.request.urlretrieve('图片的url','图片的名字')
    from lxml import etree
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="item"]//img/@alt')
    src_list = tree.xpath('//div[@class="item"]//img/@data-original')
    # for name in name_list:
    #     print(name)
    # for src in src_list:
    #     print(src)
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        # print(name,src)
        url = 'https:'+src
        # print(url)
        urllib.request.urlretrieve(url=url,filename='./站长素材图片爬取/'+name+'.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))

    for page in range(start_page,end_page+1):
        # 请求对象的定制
        request = create_request(page)
        # 获取网页的源码
        content = get_content(request)
        # 下载
        print('正在下载第{}页....'.format(page))
        download_content(content)
        print('第{}页爬取完成，请到对应文件夹查看'.format(page))
