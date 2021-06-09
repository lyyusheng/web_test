from selenium.webdriver.common.by import By

from page.base import BasePage


class UserPage(BasePage):
    """用户页面"""
    # 余额元素
    user_money_locator = (By.CSS_SELECTOR, ".color_sub")

    def get_user_money(self):
        """获取余额"""
        e = self.wait_presence_element(self.user_money_locator)
        money = e.text[0:-1].strip()  # sttrip()用来去空格
        return money
