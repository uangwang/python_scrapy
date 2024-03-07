from selenium import webdriver



driver = webdriver.Edge()

driver.get('https://www.jd.com')
content = driver.page_source
print(content)