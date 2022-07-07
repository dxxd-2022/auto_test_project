from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestWait:
    def setup(self):
        #初始化driver
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)#隐式等待
        self.driver.get("https://home.testing-studio.com/")
    def teardown(self):
        self.driver.close()
    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@title="所有分类"]').click()
        #sleep(2)#强制等待
        """
        方式一
        def wait(x):
            return len(self.driver.find_elements(By.XPATH,'//*[@class="table-heading"]'))>=1
        WebDriverWait(self.driver, 10).until(wait)
        """
        #方式二
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH,'//*[@title="过去一年、一个月、一周或一天中最活跃的话题"]').click()
