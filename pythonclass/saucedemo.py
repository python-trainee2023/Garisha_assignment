from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def teardown(self):
        self.driver.quit()


class TestSauceLogin(BaseTest):

    def test_login(self):

        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()