from appium.webdriver.common.appiumby import AppiumBy

from pages.base_pages import BasePage


class MainPage(BasePage):

    calander_btn = (AppiumBy.ID, 'com.tal.kaoyan:id/mainactivity_button_calendar')
    school_btn = (AppiumBy.ID, 'com.tal.kaoyan:id/mainactivity_button_info')
    talk_btn = (AppiumBy.ID, 'com.tal.kaoyan:id/mainactivity_button_forum')
    my_btn = (AppiumBy.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    def go_to_my_page(self):
        self.click_element(self.my_btn)


