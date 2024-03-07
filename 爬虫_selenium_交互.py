from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器对象
browser = webdriver.Edge()


# url
url = 'https://www.baidu.com'
browser.get(url)

import time
time.sleep(2)

# 获取文本框的对象
input = browser.find_element(By.ID, 'kw')

# 向文本框输入内容
input.send_keys('苏运莹')

time.sleep(2)

# 获取百度一下的按钮
button = browser.find_element(By.ID, 'su')

# 点击按钮
button.click()

time.sleep(2)

# 滑倒底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

# 获取下一页的按钮
next = browser.find_element(By.XPATH, '//a[@class="n"]')

# 点击下一页
next.click()

time.sleep(2)

# 回到上一页
browser.back()

time.sleep(2)

# 回到下一页
browser.forward()

time.sleep(2)

# 退出浏览器
browser.quit()