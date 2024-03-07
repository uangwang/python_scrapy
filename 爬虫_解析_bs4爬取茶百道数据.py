import urllib.request

url = 'https://www.chabaidao.com/home/product/index/id/2.html'

response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')

from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# //ul[@class="container"]//li/text()
name_list = soup.select('ul[class="container"] li h4')
# print(name_list)

src_list = soup.select('ul[class="container"] li img')
# for src in src_list:
#     url = 'https://www.chabaidao.com' + src.get('src')
#     print(url)

for i in range(len(name_list)):
    name = name_list[i].get_text()
    src = 'https://www.chabaidao.com' + src_list[i].get('src')
    print(name, src)
    urllib.request.urlretrieve(url = src, filename='./茶百道爬取/'+name + '.jpg')



# for name in name_list:
#     print(name.get_text())




