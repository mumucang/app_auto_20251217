
import os
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import config
from utils.driver_util import DriverUtil
from utils.log_util import LoggerUtil


class BasePage:
    def __init__(self, driver=None):
        """
        初始化BasePage类
        :param driver: WebDriver实例
        """
        if driver is None:
            self.driver = DriverUtil.get_driver()
        else:
            self.driver = driver


        self.timeout = 30  # 设置默认等待时间

        self.logger = LoggerUtil.get_logger('my_app_logger')



    def find_element(self, locator):
        """
        查找单个元素
        :param locator: 传入定位器，如(By.ID, "example")
        :return: 返回找到的元素
        """
        try:
            element = WebDriverWait(self.driver, self.timeout,0.01).until(EC.presence_of_element_located(locator))
            self.logger.info(f"Element found: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Element not found within {self.timeout} seconds: {locator}")
            return None
        except NoSuchElementException:
            self.logger.error(f"Element not found: {locator}")
            return None

    def find_elements(self, locator):
        """
        查找多个元素
        :param locator: 传入定位器，如(By.ID, "example")
        :return: 返回找到的元素列表
        """
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))
            self.logger.info(f"Elements found: {locator}")
            return elements
        except TimeoutException:
            self.logger.error(f"Elements not found within {self.timeout} seconds: {locator}")
            return []
        except NoSuchElementException:
            self.logger.error(f"Elements not found: {locator}")
            return []

    def click_element(self, locator):
        """
        点击元素
        :param locator: 传入定位器，如(By.ID, "example")
        """
        element = self.find_element(locator)
        if element:
            element.click()
            self.logger.info(f"Clicked element: {locator}")

    def input_text(self, text, locator):
        """
        向元素输入文本
        :param text: 输入的文本
        :param locator: 传入定位器，如(By.ID, "example")
        """
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Input text: '{text}' into element: {locator}")

    def get_text(self, locator):
        """
        获取元素文本
        :param locator: 传入定位器，如(By.ID, "example")
        :return: 返回元素的文本内容
        """
        element = self.find_element(locator)
        if element:
            text = element.text
            self.logger.info(f"Got text: '{text}' from element: {locator}")
            return text
        return ""

    def is_element_visible(self, locator):
        """
        判断元素是否可见
        :param locator: 传入定位器，如(By.ID, "example")
        :return: 返回布尔值，表示元素是否可见
        """
        try:
            visible = WebDriverWait(self.driver, self.timeout,0.1).until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element is visible: {locator}")
            return visible
        except TimeoutException:
            self.logger.error(f"Element not visible within {self.timeout} seconds: {locator}")
            return False
        except NoSuchElementException:
            self.logger.error(f"Element not found: {locator}")
            return False

    def wait_until_element_clickable(self, locator):
        """
        等待元素可点击
        :param locator: 传入定位器，如(By.ID, "example")
        :return: 返回可点击的元素
        """
        try:
            clickable = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
            self.logger.info(f"Element is clickable: {locator}")
            return clickable
        except TimeoutException:
            self.logger.error(f"Element not clickable within {self.timeout} seconds: {locator}")
            return None
        except NoSuchElementException:
            self.logger.error(f"Element not found: {locator}")
            return None

    def scroll_to_element(self, locator):
        """
        滚动到指定元素
        :param locator: 传入定位器，如(By.ID, "example")
        """
        element = self.find_element(locator)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.logger.info(f"Scrolled to element: {locator}")



    def switch_to_frame(self, locator):
        """
        切换到iframe
        :param locator: 传入定位器，如(By.ID, "example")
        """
        frame = self.find_element(locator)
        if frame:
            self.driver.switch_to.frame(frame)
            self.logger.info(f"Switched to frame: {locator}")

    def switch_to_default_content(self):
        """
        切换回默认内容
        """
        self.driver.switch_to.default_content()
        self.logger.info("Switched to default content")





    def take_screenshot(self, filename):
        """
        截取当前页面截图
        :param filename: 截图保存的文件名
        """
        str_time = time.strftime("%Y%m%d%H%M%S")
        path = os.path.join(config.pictures_path, f"{filename}{str_time}.png")
        self.driver.save_screenshot(path)
        self.logger.info(f"Screenshot saved as: {path}")








    def accept_alert(self):
        """
        接受警告框
        """
        alert = self.driver.switch_to.alert
        alert.accept()
        self.logger.info("Alert accepted")

    def dismiss_alert(self):
        """
        取消警告框
        """
        alert = self.driver.switch_to.alert
        alert.dismiss()
        self.logger.info("Alert dismissed")

    def get_alert_text(self):
        """
        获取警告框文本
        :return: 警告框文本
        """
        alert = self.driver.switch_to.alert
        text = alert.text
        self.logger.info(f"Alert text: {text}")
        return text

    def send_keys_to_alert(self, keys):
        """
        向警告框输入文本
        :param keys: 要输入的文本
        """
        alert = self.driver.switch_to.alert
        alert.send_keys(keys)
        self.logger.info(f"Sent keys to alert: {keys}")

    def swipe_down(self):
        """
        向下滑动
        """
        size = self.driver.get_window_size()
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8
        start_x = size['width'] * 0.5
        self.swipe(start_x, start_y, start_x, end_y)
        self.logger.info(f"向下滑动从 ({start_x}, {start_y}) 到 ({start_x}, {end_y}) 成功")

    def swipe_up(self):
        """
        向上滑动
        """
        size = self.driver.get_window_size()
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        start_x = size['width'] * 0.5
        self.swipe(start_x, start_y, start_x, end_y)
        self.logger.info(f"向上滑动从 ({start_x}, {start_y}) 到 ({start_x}, {end_y}) 成功")



    def switch_context(self, context):
        """
        切换上下文，例如从NATIVE_APP切换到WEBVIEW
        :param context: 目标上下文
        """
        try:
            self.driver.switch_to.context(context)
            self.logger.info(f"切换上下文到 {context} 成功")
        except Exception as e:
            self.logger.error(f"切换上下文到 {context} 失败: {e}")
            raise

    def swipe(self, start_x, start_y, end_x, end_y, duration=800):
        """
        滑动操作
        :param start_x: 起点x坐标
        :param start_y: 起点y坐标
        :param end_x: 终点x坐标
        :param end_y: 终点y坐标
        :param duration: 滑动时间，单位为毫秒
        """
        try:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            self.logger.info(f"滑动操作从 ({start_x}, {start_y}) 到 ({end_x}, {end_y}) 成功")
        except Exception as e:
            self.logger.error(f"滑动操作从 ({start_x}, {start_y}) 到 ({end_x}, {end_y}) 失败: {e}")
            raise

    def get_toast_text(self, msg):
        """
        获取Toast消息的文本内容
        :param toast_locator: 定位Toast消息的值
        :param timeout: 最大等待时间，默认为5秒
        :return: Toast消息的文本内容
        """
        try:
            toast_element = self.find_element((AppiumBy.XPATH,f'//*[contains(@text,"{msg}")]'))
            toast_text = toast_element.text
            self.logger.info(f"获取Toast消息的文本 {toast_text} 成功")
            print(toast_text)
            return toast_text
        except Exception as e:
            self.logger.error(f"获取Toast消息的文本失败: {e}")





