from bs4 import BeautifulSoup

# 通过解析本地文件  来将bs4的基本语法进行讲解
# 默认打开的文件的编码格式是gbk  所以在打开文件的时候需要指定编码格式
soup = BeautifulSoup(open('爬虫_解析_bs4的基本使用.html', encoding='utf-8'), 'lxml')

# 根据标签名查找节点
# 找到的是第一个符合条件的数据
print(soup.a)
# 获取标签的属性和属性值
print(soup.a.attrs)
print('----------------------------')

# bs4的一些函数
# find()  find_all()  select()  select_one()   find_parent()  find_parents()  find_next_sibling()  find_next_siblings()
print(soup.find('a'),'返回第一个符合条件的数据')
print(soup.find_all('a'),'返回所有符合条件的数据')
print(soup.find('a',title = 'a2'),'条件查询，根据title属性值为a2的数据')
# 根据class来查找数据，但是要注意class是python的关键字，所以在使用的时候需要加上下划线
print(soup.find('a',class_ = 'a1')) # class是python的关键字，所以在使用的时候需要加上下划线

# find_all  返回的是一个列表，返回了所有的li标签
print(soup.find_all('li'))
# 返回两个不同的标签，a和li
print(soup.find_all(['a','li'])) # 注意：find_all()方法的参数是一个列表，列表里面可以放多个标签名
# 返回前两个li标签
print(soup.find_all('li',limit=2)) # limit参数表示返回的数据的个数

# ----------------------------select()  select_one()---------------------------
print(soup.select('a')) # 返回所有的a标签   select返回的是一个列表，多个数据
# 带class的标签，可以通过.来查找类选择器
print(soup.select('.a1')) # 返回所有的class为a1的标签
# 带id的标签，可以通过#来查找id选择器
print(soup.select('#l1')) # 返回所有的id为a1的标签
# 根据属性选择器来查找标签
print(soup.select('a[title="a2"]')) # 返回所有的title属性值为a2的a标签
print(soup.select('li[id]')) # 返回所有带有id属性的li标签
print(soup.select('li[id="l3"]')) # 返回所有id属性值为l3的li标签

# -------层次选择器------
# 后代选择器  空格
# 找到div下面的所有的li标签
print(soup.select('div li'))

# 子代选择器  >
# 找到div下面的所有的li标签
print(soup.select('div > li'))
print(soup.select('div > ul > li'))
# 注意很多的计算机编程语言中  如果不加空格不会输出内容  但是在bs4中 不会报错  会显示内容

# 找到a标签和li标签的所有的对象
print(soup.select('a,li'))


#-------节点信息-------

# 获取节点内容
obj = soup.select('#d1')[0] # 通过id获取到的是一个列表，所以需要取出列表中的第一个元素
print(obj.get_text()) # 获取节点的内容
print(obj.string) # 获取节点的内容
#  区别：如果标签中间没有其他标签，那么两者是一样的，如果标签中间有其他标签，那么get_text()会将所有的内容都拼接起来，而string只会获取第一个标签的内容

# 节点的属性
obj2 = soup.select('#p1')[0]
print(obj2.name) # 获取节点的标签名
print(obj2.attrs) # 将属性值作为一个字典返回

# 获取节点的属性
obj3 = soup.select('#p1')[0]
print(obj3.attrs.get('class')) # 获取class属性值
print(obj3.get('class'))
print(obj3['class']) # 获取class属性值