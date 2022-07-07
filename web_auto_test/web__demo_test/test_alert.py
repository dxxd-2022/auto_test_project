import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAlert:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        time.sleep(6)
        self.driver.quit()
    def test_alert(self):
        self.driver.switch_to_frame("iframeResult")
        el_drag=self.driver.find_element(By.ID,"draggable")
        el_drog=self.driver.find_element(By.ID,"droppable")
        action=ActionChains(self.driver)
        action.drag_and_drop(el_drag,el_drog).perform()
        self.driver.switch_to_alert().accept()
        self.driver.switch_to_default_content()
        self.driver.find_element(By.XPATH,'//*[@id="submitBTN"]').click()