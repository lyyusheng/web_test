import py
import pytest
from selenium.webdriver import Chrome

from page.login import LoginPage
from page.bid import BidPage
from test_data.login import user_info_success


# one of ``"function"``(default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.
@pytest.fixture()  # scope 作用域
def login_set_up():
    """"登陆模块的fixture"""
    driver = Chrome()
    login_page = LoginPage(driver)
    yield driver, login_page
    driver.quit()


@pytest.fixture()
def bid_set_up():
    """投标模块的fixture"""
    driver = Chrome()
    login_page = LoginPage(driver)
    login_page.login(user_info_success[0]['username'], user_info_success[0]['pwd'])
    bid_page = BidPage(driver)
    yield driver, bid_page
    driver.quit()
