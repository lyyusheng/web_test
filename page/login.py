from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page.base import BasePage


class LoginPage(BasePage):
    """"登录页面封装"""
    username_locator = (By.NAME, 'phone')
    pwd_locator = (By.XPATH, "//input[@name='password']")
    url = 'http://8.129.91.152:8765/Index/login.html'

    # def __init__(self, driver):
    #     self.driver = driver
    #     self.url = 'http://8.129.91.152:8765/Index/login.html'

    def login(self, username, pwd):
        # # 1、 打开浏览器
        # driver = webdriver.Chrome()
        # 2、 访问登录页面
        self.driver.get(self.url)
        # 3、定位元素 find_element 用户名输入框 密码输入框
        # user_ele = WebDriverWait(self.driver, 20).until(
        #     ec.presence_of_element_located((By.NAME, 'phone')))
        user_ele = self.wait_presence_element(self.username_locator)
        # pwd_ele = WebDriverWait(self.driver, 20).until(
        #     ec.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        pwd_ele = self.wait_presence_element(self.pwd_locator)
        # 4、 发送用户名、密码，提交 submit
        user_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        user_ele.submit()
        # return self.driver  # 一定要记得返回

    def get_flash_info(self):
        """获取错误提示信息"""
        flash_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.form-error-info'))
        )
        return flash_ele

    def clear_user_info(self):
        """清空用户数据"""
        self.clear_username()
        self.clear_pwd()

    def clear_username(self):
        """清空用户输入框"""
        return self.get_user_info().clear()  # ？？？

    def clear_pwd(self):
        """清空密码"""
        return self.get_pwd_info().clear()

    def get_user_info(self):
        """定位手机号输入框内容"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.NAME, 'phone'))
        )
        return user_ele

    def get_pwd_info(self):
        """定位密码输入框内容"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        return user_ele
