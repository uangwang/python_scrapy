
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个浏览器对象
browser = webdriver.Edge()

url = 'https://www.baidu.com'

browser.get(url)

input = browser.find_element(By.ID, 'su')
# 获取标签的属性
print(input.get_attribute('class'))
# 获取标签的名称
print(input.tag_name)
# 获取元素的文本
a = browser.find_element(By.LINK_TEXT, '新闻')
print(a.text)

