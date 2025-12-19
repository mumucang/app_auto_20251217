from appium.webdriver.common.appiumby import AppiumBy

from pages.base_pages import BasePage
from pages.main_page import MainPage


class LoginPage(BasePage):

    username_ele = (AppiumBy.ID,"com.tal.kaoyan:id/login_email_edittext")
    password_ele = (AppiumBy.ID,'com.tal.kaoyan:id/login_password_edittext')
    login_btn = (AppiumBy.ID,'com.tal.kaoyan:id/login_login_btn')
    register_btn = (AppiumBy.ID,'com.tal.kaoyan:id/login_register_text')
    forget_btn = (AppiumBy.ID,'com.tal.kaoyan:id/login_findpassword_img')


    def login(self,username,password):
        self.input_text(username,self.username_ele)
        self.input_text(password,self.password_ele)
        self.click_element(self.login_btn)

    def get_return_text(self,msg):

        return self.get_toast_text(msg)



