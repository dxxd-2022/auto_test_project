from selenium import webdriver
from selenium.webdriver.common.by import By
class TestDemo:
    def setup(self):
        #初始化driver
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://www.baidu.com/")
    def teardown(self):
        self.driver.close()
    def test_demo(self):
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()
        self.driver.find_element(By.LINK_TEXT,"霍格沃兹测试学院 - 主页")