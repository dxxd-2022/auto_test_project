import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestTochActions:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown_class(self):
        time.sleep(10)
        self.driver.quit()
    def test_form(self):
        self.driver.find_element(By.ID,'user_login').send_keys('123')
        self.driver.find_element(By.ID,'user_password').send_keys('456')
        ele=self.driver.find_element(By.ID,'user_remember_me')
        self.driver.execute_script("arguments[0].click();", ele)
        self.driver.find_element(By.NAME,'commit').click()