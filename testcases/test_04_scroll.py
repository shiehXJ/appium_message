# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/8
# 测试用例4 滑动查找执行内容的短信


from common.page_swipe import page
from common.start_app import begin


class TestScroll:
    spc_name = "客户"

    # 滑动页面查找
    def test_scroll_msg(self):
        driver = begin.start()  # 启动APP, 获取驱动对象
        # 查找指定内容
        start = None    # 记录滑动前的源码
        end = driver.page_source  # 记录滑动后的源码

        while True:
            # 当start 与 end相等时退出循环
            if start == end:
                break
            else:
                # 找到短信内容
                result_list = driver.find_elements_by_android_uiautomator(
                    'new UiSelector().resourceId("com.android.mms:id/subject")')
                # 循环遍历已定位到的短信内容
                for result in result_list:
                    if self.spc_name in result.text:
                        # 打印出匹配到指定内容的短信内容
                        print(result.text)
                        return result, driver
                # 找不到向下滑动
                page.swipeDown(driver)
                driver.implicitly_wait(30)
                # 更新start的值。用end的值更新start 的值
                start = end
                # 更新end 的值为滑动后的page_source
                end = driver.page_source
        driver.quit()

    # 打开匹配到的第一个短信内容
    def test_click_result(self):
        result = self.test_scroll_msg()[0]

        # 获取当前元素的text内容
        get_content = result.text
        print("hhhhhhh", get_content)
        result.click()

        # 获取当前页面的所有信息
        driver = self.test_scroll_msg()[1]
        content = driver.find_elements_by_android_uiautomator(
            'new UiSelector().resourceId("com.android.mms:id/text_view")')
        for con in content:
            if con == get_content:
                assert con == get_content
