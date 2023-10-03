from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BaseClass:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ebay.com/")
        self

    def teardown(self):
        self.driver.close()


class TestLoginPage(BaseClass):
    def test_login(self):
        self.driver.find_element(By.XPATH, "//a[@_sp='m570.l1524']").click()
        username = self.driver.find_element(By.ID,"userid")
        username.send_keys("demoacc@gmail.com")
        self.driver.find_element(By.ID,"signin-continue-btn").click()
        time.sleep(2)
        password = self.driver.find_element(By.ID, "pass")
        password.send_keys("passdemO1")
        self.driver.find_element(By.ID,"sgnBt").click()

        #After login if there is tired of password site

        currenturl= self.driver.current_url
        mainurl = 'https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F'
        
        time.sleep(2)
        if(currenturl==mainurl):
            self.driver.find_element(By.ID,"dont-ask-again-link").click()
            print("Logged In Sucessful")

        else:
            print("hii")
            print("Logged In Sucessful")
        time.sleep(20)



