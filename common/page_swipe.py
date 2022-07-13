# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/8
# 滑动页面

class Swipe:

    def get_size(self, driver):
        '''获取长宽'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return x, y

    def swipe_up(self, driver, t=500, n=1):
        '''向上滑动屏幕'''
        x, y = self.get_size(driver)
        x1 = x * 0.5
        y1 = y * 0.2
        y2 = y * 0.8
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, driver, t=200, n=1):
        '''向下滑动屏幕'''
        x, y = self.get_size(driver)
        x1 = x * 0.5
        y1 = y * 0.9
        y2 = y * 0.3
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def swipe_left(self, driver, t=500, n=1):
        '''向左滑动屏幕'''
        x, y = self.get_size(driver)
        x1 = x * 0.8
        y1 = y * 0.5
        x2 = x * 0.2
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)

    def swipe_right(self, driver, t=500, n=1):
        '''向右滑动屏幕'''
        x, y = self.get_size(driver)
        x1 = x * 0.2
        y1 = y * 0.5
        x2 = x * 0.8
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)


page = Swipe()
