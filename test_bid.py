import unittest
import time
from page.bid import BidPage
from page.index import IndexPage
from page.login import LoginPage

from selenium import webdriver
import pytest
from page.user import UserPage
from test_data.bid import invest_money
from test_data.login import user_info_success
import pytest_rerunfailures

"""
前置条件
1、登录
2、有没有余额（1、查余额 2、充值 ）
3、标有没有钱
"""


class TestBid:

    # def setUp(self) -> None:
    #     """登录"""
    #     self.driver = webdriver.Chrome()
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.login(user_info_success['username'], user_info_success['pwd'])
    #     self.bid_page = BidPage(self.driver)
    #
    # def tearDown(self) -> None:
    #     self.driver.quit()
    @pytest.mark.bid
    def test_bid_success(self, bid_set_up):
        self.driver, self.bid_page = bid_set_up
        # 首页选择标的 choose_bid(),点击投标
        IndexPage(self.driver).choose_bid()
        # 定位投资输入框元素 get_bid_input_element()
        e = self.bid_page.get_bid_input_element()
        expect = float(e.get_attribute('data-amount'))
        print(expect)

        # 发送投资金额
        e.send_keys(invest_money)

        # 点击投资
        self.bid_page.click_bid_submit()

        # 点击“激活并查看”
        self.bid_page.click_alert()
        # 投资后余额
        actual_money_str = UserPage(self.driver).get_user_money()
        actual_money = float(actual_money_str)  # 不要用float加减乘除，容易出错

        # 用unittest的断言
        # self.assertTrue(int(expect * 100) - invest_money * 100) == int(actual_money) * 100
        # 用pytest的断言
        assert (int(expect * 100) - invest_money * 100) == int(actual_money) * 100


if __name__ == '__main__':
    unittest.main()
