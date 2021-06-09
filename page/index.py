from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page.base import BasePage


class IndexPage(BasePage):
    """首页类"""
    # “抢投标”元素定位
    # bid_locator = (By.XPATH, "//a[contains(@class, 'btn btn-special')]")  #出错了，用contains时要把空格去掉
    bid_locator = (By.XPATH, "//a[contains(@class, 'btn-special')]")

    # def __init__(self, driver):
    #     self.drive = driver
    user_ele_locator = (By.XPATH, "//a[@href='Member/index.html']")

    def get_user_info(self):
        """定位‘我的账户’"""
        # user_ele = WebDriverWait(self.driver, 20).until(
        #     ec.presence_of_element_located((By.XPATH, "//a[@href='/Member/index.html']"))
        # )
        user_ele = self.wait_presence_element(self.user_ele_locator)

    def choose_bid(self):
        """选择标的"""
        # 定位投标按钮
        e = self.wait_clickable_element(self.bid_locator)
        # 点击
        return e.click()


0
