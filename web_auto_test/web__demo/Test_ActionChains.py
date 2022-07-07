import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        #self.driver.get("http://sahitest.com/demo/clicks.htm")#测试test_clickcase的地址
        #self.driver.get("https://www.baidu.com")#测试test_movetoelement的地址
        #self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")#测试test_dragdrop的地址
        self.driver.get('http://sahitest.com/demo/label.htm')#测试test_keys的地址
        self.driver.maximize_window()
    def teardown_class(self):
        time.sleep(10)
        self.driver.quit()
    @pytest.mark.skip
    def test_clickcase(self):
        element_click=self.driver.find_element(By.XPATH,'//input[@value="click me"]')
        element_doubleclick=self.driver.find_element(By.XPATH,'/html/body/form/input[2]')
        element_rightclick=self.driver.find_element(By.XPATH,'/html/body/form/input[4]')
        action=ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        action.perform()

    @pytest.mark.skip
    def test_movetoelement(self):
        moveto_element=self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
        action=ActionChains(self.driver)
        action.move_to_element(moveto_element)
        action.perform()
    def test_dragdrop(self):
        element_source=self.driver.find_element(By.XPATH,'//*[@id="dragger"]')
        element_target=self.driver.find_element(By.XPATH,'//div[@class="item"][1]')
        action=ActionChains(self.driver)
        # action.drag_and_drop(element_source,element_target).perform()#方式一
        # action.click_and_hold(element_source).release(element_target).perform()#方式二
        action.click_and_hold(element_source).move_to_element(element_target).release().perform()#方式三
    def test_keys(self):
        ele1=self.driver.find_element(By.XPATH,'//body/label[1]/input[@type="textbox"]')
        ele1.click()
        action=ActionChains(self.driver)
        action.send_keys("username")
        action.send_keys(Keys.SPACE)
        action.send_keys(":tom")
        action.send_keys(Keys.BACK_SPACE).perform()
