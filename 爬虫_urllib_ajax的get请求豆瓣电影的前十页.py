import urllib.request
import urllib.parse
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20

# page   1   2   3   4   5
# start  0   20  40  60  80
# start = (page-1)*20

# 请求对象的定制

# 获取响应数据

# 下载数据


def creat_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    data = {
        'start':(page-1)*20,
        'limit':20
    }

    data = urllib.parse.urlencode(data) # get后面不需要编码

    url = base_url + data

    # print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download_content(content,page):
    with open('douban'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))

    for page in range(start_page,end_page+1):
        # 每一页都有自己的请求对象的定制
        request = creat_request(page)
        # 获取响应数据
        content = get_content(request)
        # 下载数据
        download_content(content,page)




