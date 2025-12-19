import os
import time

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import platformName, appium_server_url


class DriverUtil:
    @staticmethod
    def get_driver():
        options = AppiumOptions()
        caps={
            'platformName': platformName,
            'platformVersion': '9',
            'deviceName': 'emulator-5558',
            'appPackage': 'com.tal.kaoyan',
            'appActivity': 'com.tal.kaoyan.ui.activity.SplashActivity',
            'automationName': 'uiautomator2',
            'noReset': True
        }
        options.load_capabilities(caps)
        os.system("adb shell pm clear com.tal.kaoyan")
        driver = webdriver.Remote(appium_server_url,options=options)
        ele = WebDriverWait(driver, 10,0.1).until(expected_conditions.presence_of_element_located((AppiumBy.ID, "android:id/button2")))
        ele.click()
        width = driver.get_window_size()["width"]
        height=driver.get_window_size()["height"]
        time.sleep(1)
        for i in range(2):
            driver.swipe(0.9 * width, 0.5 * height, 0.1 * width, 0.5 * height, duration=100)
        ele = WebDriverWait(driver, 10,0.1).until(expected_conditions.presence_of_element_located((AppiumBy.ID, "com.tal.kaoyan:id/activity_splash_guidfinish")))
        ele.click()
        return driver


if __name__ == '__main__':
    DriverUtil.get_driver()