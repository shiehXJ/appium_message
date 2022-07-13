# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/10


from common.start_app import begin
from common.send_message import message


class TestPhone:
    def test_01_send_phone(self):
        driver = begin.start()

        # 给指定手机号码发送指定消息
        message.specific_number()

        # 返回上一页
        begin.return_home()

        # 检查刚才发送的短信已经发送完成  ---在信息列表搜索刚发送短信的内容，并点击进入号码
        result_list = driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.android.mms:id/subject")')
        for result in result_list:
            if result.text == "指定内容":
                result.click()
                result_phone = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.mms:id/sub_title")')
                assert result_phone == "19917182801"
            else:
                print("未查找到相关内容，请确定短信是否发送成功")

        driver.quit()
