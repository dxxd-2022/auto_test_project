from selenium import webdriver
from selenium.webdriver.common.by import By
class TestWindows:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://www.baidu.com/")
    def teardown(self):
        self.driver.quit()
    def test_windows(self):
        self.driver.find_element(By.ID,'s-top-loginbtn').click()
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__regLink').click()
        #print(self.driver.current_window_handle)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__userName').send_keys('htdcurry')
        self.driver.switch_to_window(windows[0])
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__regLink').click()
