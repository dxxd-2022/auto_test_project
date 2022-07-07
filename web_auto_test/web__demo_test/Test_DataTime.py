import time
from selenium import webdriver
class TestDataTime:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.12306.cn/index/')
        self.driver.maximize_window()
    def teardown_class(self):
        time.sleep(10)
        self.driver.quit()
    def test_datatime(self):
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script("return document.getElementById('su')")
        self.driver.execute_script("document.getElementById('train_date').value='2021/12/3'")