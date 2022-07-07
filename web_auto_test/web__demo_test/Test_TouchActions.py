import time

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

class TestTochActions01():
    def setup(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver=webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    # def teardown(self):
    #     self.driver.quit()
    def test_touchaction_scrollbottom(self):
        self.driver.get("http://www.baidu.com")
        el=self.driver.find_element(By.ID,'kw')
        el_search=self.driver.find_element(By.ID,'su')
        print(type(el))
        el.send_keys("selenium测试")
        el_search.click()
        action=TouchActions(self.driver)
        action.tap(el_search)
        action.perform()
        action.scroll_from_element(el,0,10000).perform()



        

