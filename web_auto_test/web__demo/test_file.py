from selenium import webdriver
from selenium.webdriver.common.by import By
class TestFile:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://www.baidu.com/")
    #def teardown(self):
        #self.driver.quit()
    def test_up_file(self):
        self.driver.find_element(By.XPATH,'//*[@class="soutu-btn"]').click()
        self.driver.find_element(By.XPATH,'//*[@class="upload-pic"]').send_keys('D:\pythonProject_API_request\web_test\风景.jpg')
