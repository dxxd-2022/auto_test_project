from selenium.webdriver.common.by import By
from web_test.Page_Object.Po.base import Base
from web_test.Page_Object.Po.contact_page import ContactPage


class MainPage(Base):
    def goto_contact(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        # self.driver.implicitly_wait(3)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #self.driver.find_element(By.ID, "menu_contacts").click()
        self.find_and_click(By.ID,"menu_contacts")
        return ContactPage(self.driver)