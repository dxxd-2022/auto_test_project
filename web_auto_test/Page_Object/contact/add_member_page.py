from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from web_test.Page_Object.Po.base import Base

class AddMemberPage(Base):
    def edit_member(self):
        from web_test.Page_Object.Po.contact_page import ContactPage
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'username')))
        # self.driver.find_element(By.ID,'username').send_keys("库利南")
        # self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("KLN123456")
        # self.driver.find_element(By.ID,"memberAdd_biz_mail").send_keys("147369@qq.com")
        # self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()
        self.find(By.ID,'username').send_keys("库利南")
        self.find(By.ID,"memberAdd_acctid").send_keys("KLN123456")
        self.find(By.ID,"memberAdd_biz_mail").send_keys("147369@qq.com")#企业微信后面对添加联系人中的企业邮箱加了校验，所以添加不成功
        self.find_and_click(By.CSS_SELECTOR,".js_btn_save")
        return ContactPage(self.driver)