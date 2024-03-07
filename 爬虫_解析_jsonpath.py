import jsonpath
import json

obj = json.load(open('爬虫_解析_jsonpath.json', 'r', encoding='utf-8'))
print(obj)
# 书店所有的书的作者
author_list = jsonpath.jsonpath(obj, '$.store.book[0,3].author') # 通过下标获取第几本书的作者
print(author_list)

# 书店所有的作者
author_list2 = jsonpath.jsonpath(obj, '$..author') # 通过下标获取第几本书的作者
print(author_list2)

# store下的所有的元素
store_list = jsonpath.jsonpath(obj, '$.store.*')
print(store_list)

# 所有的价格
price_list = jsonpath.jsonpath(obj, '$..price')
print(price_list)

# 第三本书的价格
book_price = jsonpath.jsonpath(obj, '$..book[2].price')
print(book_price)

# 最后一本书的作者
book_author = jsonpath.jsonpath(obj, '$..book[-1:].author')
print(book_author)

# 前两本书的作者
book_author2 = jsonpath.jsonpath(obj, '$..book[:2].author')
print(book_author2)

# 过滤出带有isbn的书
book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]') # 条件过滤需要在（）前面加上？号
print(book_list)

# 过滤出价格大于10的书
book_list2 = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(book_list2)
