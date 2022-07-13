# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/10


class Message:

    def create_msg(self):
        # 新建信息
        self.driver.find_element_by_accessibility_id("新建信息").click()
        self.driver.implicitly_wait(30)

    # 给指定号码发送短信
    def specific_number(self, phone):
        self.create_msg()

        # 选择收件人输入框输入手机号码
        el1 = self.driver.find_element_by_accessibility_id("收件人：")
        el1.send_keys("19917182801")
        self.driver.implicitly_wait(30)

        # 输入发送的短信内容
        el2 = self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        el2.send_keys("给指定手机号码发送信息")
        self.driver.implicitly_wait(30)

        # 点击发送
        el3 = self.driver.find_element_by_id("com.android.mms:id/send_button_sms")
        el3.click()
        self.driver.implicitly_wait(30)

    # 从通讯中选择联系人发送
    def contact_number(self, contact):
        pass


message = Message()
