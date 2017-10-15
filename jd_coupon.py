#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time

# 不设置个人目录的话，每次重新载入太费时间
option = webdriver.ChromeOptions()
#chrome地址栏输入 chrome://version/ 查看“个人资料路径” 拷贝到下面替换
option.add_argument('--user-data-dir=C:\Users\ThinkPad\AppData\Local\Google\Chrome\User Data\Profile 1') #设置成用户自己的数据目录

browser = webdriver.Chrome(chrome_options=option)

#不设置个人资料路径
#browser = webdriver.Chrome()

browser.maximize_window();
browser.get('http://www.jd.com')

assert "JD" in browser.title #正常 无异常抛出

# login
def login(user_name, user_passwordd):
    # 载入缓存的话，请登录前面带用户id，采用部分匹配文字
    if browser.find_element_by_partial_link_text('请登录'):
        browser.find_element_by_partial_link_text('请登录').click()
        print(u"请登录")
    if browser.find_element_by_link_text('账户登录'):
        browser.find_element_by_link_text('账户登录').click()
        print(u'账户登录')
    if browser.find_element_by_id('loginname'):
        browser.find_element_by_id('loginname').clear()
        browser.find_element_by_id('loginname').send_keys(user_name)
        print('loginname')
    if browser.find_element_by_id('nloginpwd'):
        browser.find_element_by_id('nloginpwd').send_keys(user_passwordd)
        print('nloginpwd')
    if browser.find_element_by_id('loginsubmit'):
        browser.find_element_by_id('loginsubmit').click()
        print('loginsubmit')
    time.sleep(1)

    now = datetime.datetime.now()
    print(now)
    print("login successful", now.strftime('%Y-%m-%d %H:%M:%S'))

# for coupon
def get_coupon_on_time(coupon_time, coupon_id):
    print('in get_coupon_on_time',coupon_time)
    #打开优惠券页面
    browser.get('https://a.jd.com/')
    #点击分类 手机数码 为例
    if browser.find_element_by_link_text('手机数码'):
        browser.find_element_by_link_text('手机数码').click()
        print(u'手机数码')
    #time.sleep(1)
    # //*[@id="quanlist"]/div[2]/div[1]/div[4]/div[1]/a
    # 例子 <a href="#none" class="btn btn-def"
    #       rel="3cf715bb8db038ecd73c8e1a6b3ea071fa18d8f6bfe4abecadec203f1d57f1f5d6629c897d03e7318f30b49dbe4b3ea0"
    #       data-batch="46935945" data-type="1"
    #       data-url="//search.jd.com/Search?coupon_batch=46935945"><b></b>
    #       <span class="txt">立即领取</span></a>
    # 考虑以 data-batch 为索引查找
    # 已被领取或者未到时间不显示领取按钮


    while True:
        print ('in 1st wile true')
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == coupon_time:
            while True:
                print('in 2nd while true')
                try:
                    if isDisplay(coupon_id):
                        browser.find_element_by_xpath("//a[@data-batch='47159087']").click()
                except:
                    print(u'找不到这个优惠券咯')
                    time.sleep(0.1)
        time.sleep(0.1)



    # def isElement(self,identifyBy,locatorString):
    #    flag = False
    #    try:
    #      if identifyBy == "id":
    #         driver.find_element_by_id("kw")
    #         flag = True
    #      elif identifyBy == "xpath":
    #          ......
    #    except NoSuchElementException,e
    #         print u"未找到元素"
    #         flag = False
    #    return flag

def isDisplay(coupon_id):
    isDisplayed = False
    xpath = "//a[@data-batch='"+coupon_id + "']"
    print(xpath)
    try:
        driver.find_element_by_xpath(xpath).is_displayed()
    except:
        print u"未找到元素"
        isDisplayed = False
    else:
        print u"元素存在"
        isDisplayed = True
    return isDisplayed

isDisplay('47159087')
login('xxxx@xxx.com','xxxxxxx')
get_coupon_on_time('2017-08-15 21:56:22','coupon_id')
