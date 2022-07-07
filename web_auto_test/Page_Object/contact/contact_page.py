from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from auto_test_project.web_auto_test.Page_Object.Po.add_member_page import AddMemberPage
from auto_test_project.web_auto_test.Page_Object.Po.base import Base


class ContactPage(Base):
    def click_add_member(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        # self.driver.implicitly_wait(3)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@class='ww_operationBar']/a[1]")))
        #self.driver.find_element(By.XPATH,"//*[@class='ww_operationBar']/a[1]").click()
        self.find_and_click(By.XPATH,"//*[@class='ww_operationBar']/a[1]")
        return AddMemberPage(self.driver)
    def get_member_name(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        name_list=[]
        #eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(1)")
        eles=self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(1)")
        print(eles)
        for ele in eles:
            name_list.append(ele.get_attribute("title"))
        return name_list