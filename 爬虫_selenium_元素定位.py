from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()

url = 'https://www.baidu.com'
browser.get(url)

# 元素定位

# 通过id定位
button1 = browser.find_element(By.ID, 'su')
print(button1)

# 通过name定位
button2 = browser.find_element(By.NAME, 'wd')
print(button2)

# 通过xpath定位
button3 = browser.find_element(By.XPATH, '//input[@id="su"]')
print(button3)

# 通过标签名定位
button4 = browser.find_elements(By.TAG_NAME, 'input')
print(button4)

# 通过bs4的语法获取元素
button5 = browser.find_element(By.CSS_SELECTOR, '#su')
print(button5)

# 通过Link_text定位
button6 = browser.find_element(By.LINK_TEXT, '新闻')
print(button6)
