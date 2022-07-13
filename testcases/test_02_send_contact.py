# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/10


import random
from bs4 import BeautifulSoup

from common.start_app import begin


class TestContact:
    def test_02_send_contact(self):

        driver = begin.start()

        # 新建信息
        driver.find_element_by_accessibility_id("新建信息 ").click()
        driver.implicitly_wait(30)

        # 选择通讯录-联系人-输入框输入手机号码
        driver.find_element_by_id("com.android.mms:id/recipients_picker").click()
        driver.implicitly_wait(30)

        # 获取到联系人列表
        driver.find_element_by_id("com.huawei.contacts:id/contact_multi_selection_tab_contacts").click()
        driver.implicitly_wait(30)

        # 列表为空---不为空
        app = driver.page_source
        bs4 = BeautifulSoup(app)
        contact_list = bs4.find(id, "android:id/list")
        if len(contact_list) == 0:
            print("无该联系人，请重新输入")
        else:
            # 随机选择一个联系人
            index = random.randint(0, len(contact_list))
            contact = driver.find_elements_by_id("android:id/list")[index]
            phone = contact.get_attribute("text")
            contact.click()

        # 点击确定
        driver.find_element_by_id("android:id/icon2").click()
        driver.implicitly_wait(30)

        # 输入发送的短信内容
        el2 = driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        el2.send_keys("从通讯录选择联系人发送信息")
        driver.implicitly_wait(30)

        search = driver.find_element_by_id("com.android.mms:id/search_text")
        search.send_keys("phone")

        # 返回首页

        driver.quit()
