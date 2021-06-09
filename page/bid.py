from selenium.webdriver.common.by import By

from page.base import BasePage


class BidPage(BasePage):
    """"投资页面封装"""
    # 投资输入框定位
    bid_input_locator = (By.XPATH, "//input[contains(@class, 'form-control invest-unit-investinput')]")
    # “投标”按钮元素定位
    bid_submit_locator = (By.XPATH, "//button[contains(@class,'btn-special height_style')]")
    # "查看并激活"按钮定位
    alert_active_locator = (By.XPATH, "//div[contains(@class,'layui-layer-content')]//button[contains(text(),'查看并激活')]")

    def get_bid_input_element(self):
        return self.wait_presence_element(self.bid_input_locator, timeout=20)

    def click_bid_submit(self):
        """点击投标按钮"""
        e = self.wait_clickable_element(self.bid_submit_locator)
        e.click()

    def click_alert(self):
        """点击激活并查看按钮"""
        e = self.wait_clickable_element(self.alert_active_locator)
        # 点击
        e.click()
