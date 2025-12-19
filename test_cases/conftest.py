import pytest

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def get_login_page():
    login_page = LoginPage()
    yield login_page

