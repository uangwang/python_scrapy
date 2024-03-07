from lxml import etree

# xpath解析
# （1） 本地文件                                                  etree.parse('本地文件路径')
# （2） 服务器响应的数据   response.read().decode('utf-8') *****    etree.HTML('服务器响应的数据')

# xpath解析本地文件
tree = etree.parse('爬虫_解析_xpath的基本使用.html')
# print(tree)

# (tree.xpath('//bofy')

# 查找ul下面的li
li_list = tree.xpath('//body/ul/li/text()')
# 判断列表的长度
print(li_list)
print(len(li_list))

# 查找所有id的属性的li标签
li_list_id= tree.xpath('//ul/li[@id="li"]/text()')
print(li_list_id)

# 查找到id为l1的li标签的class属性值
li_list_class = tree.xpath('//ul/li[@id="l1"]/@class')
print(li_list_class)

# 查询id中包含l的li标签
li_list_l = tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_list_l)

# 查询id的值为l开头的li标签
li_list_l1 = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')
print(li_list_l1)

# 查询id为l1和class为c1的li标签
li_list_l1_c1 = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
print(li_list_l1_c1)