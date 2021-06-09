from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging


class BasePage:
    """

    """

    def __init__(self, driver: Chrome):  # 后面截图不提示，加了Chrome才提示，要import
        self.driver = driver

    def wait_presence_element(self, locator, timeout=10):
        """等待元素出现"""
        try:
            user_ele = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )
            return user_ele
        except Exception as e:
            # logger
            logging.error('元素定位失败')
            # 截屏
            self.driver.save_screenshot('test.jpg')

    def wait_clickable_element(self, locator):
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(locator)
            # ec.element_to_be_clickable((By.XPATH, "//a[@href='/member/index.html']"))
        )
        return user_ele

    def switch(self):
        """窗口、iframe、alert"""
        pass

    def click(self):
        pass

    def send_keys(self):
        pass
