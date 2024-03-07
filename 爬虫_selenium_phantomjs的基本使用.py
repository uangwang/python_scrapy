from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.PhantomJS()

url = 'https://www.baidu.com'

browser.get(url)
browser.save_screenshot('baidu.png')
