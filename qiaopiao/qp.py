# coding:utf-8
# author:chengchen
# time:2018.8.7 
from selenium.webdriver.support.ui import Select 
from selenium import webdriver 
from winsound import Beep 
import time, sys
#报错的话，添加以下代码，忽略报错
# options = webdriver.FirefoxOptions()
# options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
# driver=webdriver.Chrome(chrome_options=options)

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://kyfw.12306.cn/otn/login/init")
driver.find_element_by_id('username').send_keys('18151032084')

#为了不泄露密码，就没自动化，需要人工干涉，这部分后面会用cookie保持sessions会话机制。
raw_input('登录界面，请输入密码登录后，按回车')

driver.get("https://kyfw.12306.cn/otn/leftTicket/init")

# 输入起始站点和终点
fromEle = driver.find_element_by_id('fromStationText')
fromEle.click()
fromEle.clear()
fromEle.send_keys(u'南京\n')

toEle = driver.find_element_by_id('toStationText')
toEle.click()
toEle.clear()
toEle.send_keys(u'镇江\n')

timeSelect = Select(driver.find_element_by_id('cc_start_time'))
timeSelect.select_by_visible_text('06:00--12:00')

#找到后天那个元素
tomorrow = driver.find_element_by_css_selector('#date_range li:nth-child(3)')

i=0
while True:
    i += 1
    isGet = False  # 设置为没有找到
    tomorrow.click()
    # 选择二等座有票的车
    xpath = '//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'
    interested = ['G7035', 'G7039', 'G1377', 'G7355']
    theTrains = driver.find_elements_by_xpath(xpath)

    for one in theTrains:
        name = one.text
        if name in interested:
            isGet = True
            print("you yu piao\n" + name)
            # 找到当前元素的上层节点
            target = one.find_elements_by_xpath('../../../../../td[last()]')
            firstbutton=target[0]
            firstbutton.click()

            time.sleep(4)

            driver.find_element_by_id('normalPassenger_0').click()
            driver.find_element_by_id('submitOrder_id').click()

            Beep(1500, 2000)
            sys.exit()

        if isGet==False:
            print('{%i}轮搜索没有找到'%i)

    time.sleep(5)