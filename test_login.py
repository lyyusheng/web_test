"""测试登录功能"""
import time
import unittest

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page.login import LoginPage
from page.base import BasePage
from test_data.login import user_info_success, user_info_error, user_info_authorize
from page.index import IndexPage


@pytest.mark.usefixtures('login_set_up')    # 类使用fixture,具体有待研究
class TestLogin:  # 继承两个

    # def setUp(self) -> None:
    #     # 浏览器初始化
    #     self.driver = Chrome()
    #     # 初始化登陆页面
    #     self.login_page = LoginPage(self.driver)
    #
    # def tearDown(self) -> None:
    #     self.driver.quit()
    @pytest.mark.login
    @pytest.mark.parametrize('data', user_info_success)
    def test_login_success(self, data, login_set_up):
        # # 浏览器初始化
        # self.driver = Chrome()
        # # 初始化登陆页面
        # self.login_page = LoginPage(self.driver)
        self.driver, self.login_page = login_set_up
        # self.login_page.login('18300070752', 'lys123456')  # login()记得返回driver，继承了BasePage则不用
        self.login_page.login(data['username'], data['pwd'])
        user_info_locator = (By.XPATH, "//a[@href='/Member/index.html']")
        # 5、 断言
        # user_ele = browser.find_element_by_xpath("//a[@href='/Member/index.html']")
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/Member/index.html']")))
        # user_ele = IndexPage(self.driver).get_user_info()

        assert (data["expected"] in user_ele.text)
        # self.driver.quit()

    # 手机号为空：请输入手机号码
    # 手机号格式不正确：请输入正确的手机号
    # 密码为空：请输入密码

    # 错误信息定位： .form-error-info
    @pytest.mark.empty
    @pytest.mark.parametrize('data', user_info_error)
    @pytest.mark.login
    def test_login_error1(self, data, login_set_up):
        # # 浏览器初始化
        # self.driver = Chrome()
        # # 初始化登陆页面
        # self.login_page = LoginPage(self.driver)
        self.driver, self.login_page = login_set_up
        # self.login_page.login('18300070752', '')
        self.login_page.login(data['username'], data['pwd'])
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='form-error-info']")))
        assert (data["expected"] in user_ele.text)
        self.driver.quit()

    # @pytest.mark.skip(reason="暂时不测")
    @pytest.mark.login
    @pytest.mark.parametrize('data', user_info_authorize)
    def test_login_error2(self, data, login_set_up):
        # # 浏览器初始化
        # self.driver = Chrome()
        # # 初始化登陆页面
        # self.login_page = LoginPage(self.driver)
        self.driver, self.login_page = login_set_up
        # self.login_page.login('', 'lys123456')
        self.login_page.login(data['username'], data['pwd'])
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='layui-layer-content']")))
        assert (data["expected"] in user_ele.text)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()  # 不加这个运行没结果
# 报错：AttributeError: 'NoneType' object has no attribute 'find_element'
# 原因： login.py没有self.drive
