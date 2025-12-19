from appium.webdriver.common.appiumby import AppiumBy

from pages.base_pages import BasePage


class MyPage(BasePage):


    set_ele = (AppiumBy.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    log_out_ele = (AppiumBy.ID, 'com.tal.kaoyan:id/setting_logout_text')
    accept_btn = (AppiumBy.ID, 'com.tal.kaoyan:id/tip_commit')

    def click_setting(self):
        self.click_element(self.set_ele)

    def click_logout(self):
        self.click_element(self.log_out_ele)

    def click_accept(self):
        self.click_element(self.accept_btn)



