import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestTochActions:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
    def teardown_class(self):
        time.sleep(15)
        self.driver.quit()
    def test_js_scroll(self):
        self.driver.find_element(By.ID,'kw').send_keys("selenium测试")
        ele=self.driver.execute_script("return document.getElementById('su')")
        ele.click()#这里如果需要执行点金操作，必须在上面将定位到的元素返回（return）,f否则会报错
        self.driver.execute_script("document.documentElement.scrollTop=1000")
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//div[@class="page-inner_2jZi2"]/a[10]').click()