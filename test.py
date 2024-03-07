from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def login(browser):
    print('开始登录功能！')
    try:
        # 获取输入框对象
        input1 = browser.find_element(By.ID, 'username')
        input2 = browser.find_element(By.ID, 'password')
        # 向输入框输入内容
        input1.send_keys('202119121729')
        time.sleep(1)
        input2.send_keys('Wxw020601.')
        time.sleep(1)
        # 模拟按下回车键登录
        input2.send_keys('\n')
        print('登录成功！')
        time.sleep(2)
    except:
        print('登录失败！')
        browser.quit()
        return False
    return True

def grade_query(browser):
    print('开始成绩查询功能！')
    # 点击个人成绩
    button_grade = browser.find_element(By.XPATH, '//div[@class="scrollbar"]//div[@class="zl-scrollContentDiv"]//li[6]')
    button_grade.click()
    time.sleep(1)
    # 点击课程成绩
    button_course = browser.find_element(By.XPATH, '//div[@class="scrollbar"]//div[@class="zl-scrollContentDiv"]//li[6]//ul//li[1]')
    button_course.click()
    time.sleep(1)
    # 点击成绩查询
    button_query = browser.find_element(By.XPATH, '//div[@class="scrollbar"]//div[@class="zl-scrollContentDiv"]//li[6]//ul//li[1]//ul//li[1]//div//span')
    button_query.click()
    time.sleep(1)
    print('成绩查询成功！')
    # 下滑
    js_bottom = 'document.documentElement.scrollTop=100000'
    browser.execute_script(js_bottom)
    time.sleep(2)
    # 退出浏览器
    # browser.quit()

if __name__ == '__main__':
    # 创建一个浏览器对象
    url = 'https://cas.paas.cdut.edu.cn/cas/login?service=http%3A%2F%2Fjw.cdut.edu.cn%2Fsso%2Flogin.jsp%3FtargetUrl%3Dbase64aHR0cDovL2p3LmNkdXQuZWR1LmNuL0xvZ29uLmRvP21ldGhvZD1sb2dvblNTT2NkbGdkeA%3D%3D'
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(1)
    # 登录
    if login(browser):
        fun_choice = input('请输入你需要的功能：')
        if fun_choice == '1':
            # 成绩查询功能
            grade_query(browser)
        else:
            print('输入有误！')
            browser.quit()

