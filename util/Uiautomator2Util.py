# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
import sys
import uiautomator2 as u2
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DingTalk(object):

    def __init__(self):
        self.conn = u2.connect()

    def unlock(self):  # 解锁手机屏幕
        self.conn.screen_on()
        logger.info("判断手机是否在锁屏状态")
        if self.conn(resourceId="com.android.systemui:id/notification_stack_scroller").exists():  # 判断手机是否在锁屏状态
            logger.info("锁屏状态，执行解锁")
            self.conn.swipe_points([(0.485, 0.708), (0.481, 0.286)], 0.05)  # 滑动解锁界面
            time.sleep(1)
            logger.info("判断是否存在图案锁")
            if self.conn(resourceId="com.android.systemui:id/lockPatternView").exists():  # 判断是否存在图案锁
                logger.info("存在，需要解图案锁")
                self.conn.swipe_points(
                    [(296, 1300), (296, 1719), (296, 2129), (758, 1695), (1120, 1300), (1120, 1719), (1120, 2129),
                     (758, 1300),
                     (758, 2129)],
                    0.05)  # 解九宫图案锁（需要修改自己的图案锁坐标）
                time.sleep(1)
            else:
                logger.info("不存在，滑动解锁成功")
        else:
            logger.info("手机未锁屏不用解锁")

    def dingtalk(self):
        self.unlock()
        self.conn.app_start('com.alibaba.android.rimet')
        self.conn.sleep(5)
        if self.conn(resourceId="com.alibaba.android.rimet:id/btn_next").exists():  # 判断是否需要登录
            logger.info("需要登录")
            self.login()  # 执行登录dd账户
        self.conn.sleep(10)
        self.daka()

    def login(self):  # 登录dd账号
        logger.info("输入账号")
        time.sleep(1)
        self.conn(resourceId="com.alibaba.android.rimet:id/et_phone_input").click()
        self.conn.sleep(1)
        self.conn(resourceId="com.alibaba.android.rimet:id/et_phone_input").clear_text()  # 这里是清除指定元素的内容
        self.conn.sleep(1)
        self.conn(resourceId="com.alibaba.android.rimet:id/et_phone_input").set_text('xxxxxxx')  # 这里是在指定元素中输入dd账号
        self.conn.sleep(1)
        self.conn.info("输入密码")
        self.conn(resourceId="com.alibaba.android.rimet:id/et_pwd_login").click()
        self.conn(resourceId="com.alibaba.android.rimet:id/et_pwd_login").clear_text()  # 这里是清除指定元素的内容
        self.conn.sleep(1)
        self.conn(resourceId="com.alibaba.android.rimet:id/et_pwd_login").set_text('xxxxxxx')  # 这里是在指定元素中输入dd密码#
        self.conn.click(1384, 1434)
        self.connsleep(1)
        logger.info("登录")
        self.conn(resourceId="com.alibaba.android.rimet:id/btn_next").click()
        self.conn.sleep(1)

    def daka(self):
        logger.info("点击工作台")
        # 工作台
        self.conn(text="工作台").click()
        self.conn.sleep(3)
        logger.info("选择公司")
        # 选择公司
        self.conn(resourceId="com.alibaba.android.rimet:id/menu_current_company").click()
        self.conn.sleep(2)
        self.conn(text="xxxxxxx").click()
        self.conn.sleep(2)
        logger.info("点击考勤打卡")
        self.conn(text="考勤打卡").click()


if __name__ == '__main__':
    DingTalk = DingTalk()
    DingTalk.dingtalk()
