from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestAddContact:
    def setup(self):
        opt=webdriver.ChromeOptions()
        opt.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=opt)#以上步骤是对浏览器的复用，然后传递给driver
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def teardown(self):
        self.driver.close()
    def test_add_contact(self):
        #以下代码为企业微信的添加联系人的案例（流水线代码-->改造代码见Po封装的）
        self.driver.find_element(By.ID,"menu_contacts").click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@class='ww_operationBar']/a[1]")))
        self.driver.find_element(By.XPATH,"//*[@class='ww_operationBar']/a[1]").click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'username')))
        self.driver.find_element(By.ID,'username').send_keys("库利南")
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("KLN123456")
        self.driver.find_element(By.ID,"memberAdd_biz_mail").send_keys("147369@qq.com")
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="member_colRight_memberTable_th"][1]')))
        eles=self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(1)")
        print(eles)
        for ele in eles:
            if ele.get_attribute("title")=="库利南":
                return True