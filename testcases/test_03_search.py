# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/10
# 测试用例3：搜索指定的短信内容


from common.start_app import begin


class TestSearch:
    def test_03_search(self):

        driver = begin.start()

        # 搜索信息
        driver.find_element_by_id("com.android.mms:id/search_text").click()
        driver.find_element_by_id("com.android.mms:id/search_text").send_keys("rrrrrrr")
        driver.implicitly_wait(30)

        # 找到对应的短信
        try:
            message_list = driver.find_elements_by_android_uiautomator(
                'new UiSelector().resourceId("com.android.mms:id/subtitle")')

            assert len(message_list) > 0
            for mes in message_list:
                print(mes.text)
        except Exception:
            print("没有匹配的结果")
            exit()

        driver.quit()
