import os.path
import time

import allure
import pytest

from config import datas_path
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.my_page import MyPage
from utils.read_excle_util import ReaderExcelUtil

login_datas = ReaderExcelUtil.read_excel(os.path.join(datas_path,"app_datas.xlsx"),"login_datas")
@allure.feature("登录模块")
@allure.story("登录功能")
class TestLogin:

    @pytest.mark.parametrize("title,username,password,jieguo",login_datas)
    @allure.title("[{title}]")
    def test_login(self,get_login_page,title,username,password,jieguo):
        with allure.step("登录"):
            get_login_page.login(username,password)
            text = get_login_page.get_return_text(jieguo)
        with allure.step("验证结果"):
            if text=="我":
                main_page = MainPage(get_login_page.driver)
                main_page.go_to_my_page()
                my_page = MyPage(get_login_page.driver)
                my_page.click_setting()
                my_page.click_logout()
                my_page.click_accept()
                time.sleep(1)
                assert True
            else:
                if text:
                    assert True
                else:
                    assert False


        # if text:
        #     assert True
        # else:
        #     assert False
        # if get_login_page.find_element(MainPage.my_btn):
        #     my_text = get_login_page.login_success()
        #     main_page = MainPage(get_login_page.driver)
        #     main_page.go_to_my_page()
        #     my_page = MyPage(get_login_page.driver)
        #     my_page.click_setting()
        #     my_page.click_logout()
        #     my_page.click_accept()
        #     assert jieguo in my_text
        # else:
        #     text = get_login_page.login_failure(jieguo)
        #     if text:
        #         assert True
        #     else:
        #         assert False



        # if get_login_page.login_success():
        #     assert jieguo in get_login_page.login_success()
        # else:


    # def test_login_success(self):
    #
    #     self.login_page.login("zhangfei666","zhang123")

    #
    # def test_login_null_username_failure(self):
    #
    #     self.login_page.login("", "zhang123")
    #
    #
    # def test_login_null_password_failure(self):
    #     self.login_page.login("zhangfei666", "")
    #
    # def test_wrong_username_password_failure(self):
    #     self.login_page.login("zhangfei666", "")