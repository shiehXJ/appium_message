# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/10
# 打开手机短信APP ----以华为手机的信息为准

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Launch:
    url = "http://127.0.0.1:4723/wd/hub"
    desired_cap = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "192.168.3.4:5555",
        "appPackage ": "com.android.mms",
        "appActivity": "./ui.ConversationList",
        "automationName": "UiAutomator2",
        "noReset": True
    }

    # 启动APP,返回webdriver对象
    def __init__(self):
        self.driver = webdriver.Remote(self.url, self.desired_cap)

    def start(self):
        """
        启动华为手机的华为信息APP
        :return: ->driver
        """
        # APP的配置
        desired_cap = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "192.168.3.4:5555",
            "appPackage ": "com.android.mms",
            "appActivity": "./ui.ConversationList",
            "automationName": "UiAutomator2",
            "noReset": True
        }
        return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_cap)

    # 返回上一页
    def return_home(self):
        # 发送完成回到信息列表页
        self.driver.find_element_by_id("com.android.mms:id/bt_cancel").click()
        # driver.implicitly_wait(30)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "com.android.mms:id/search_text")))


begin = Launch()
