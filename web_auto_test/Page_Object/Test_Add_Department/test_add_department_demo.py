from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

#企业微信添加部门
class TestDemo:
    def test_demo(self):
        opt=webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=opt)#浏览器复用
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.find_elements(By.CSS_SELECTOR,".frame_nav_item_title")[1].click()#点击通讯录
        self.driver.find_element(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()  # 点击加号
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_party").click()  # 点击添加部门
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys("广东宏远队")  # 点击编辑部门信息输入框
        self.driver.find_element(By.CSS_SELECTOR, ".js_parent_party_name").click()#点击部门
        self.driver.find_elements(By.CSS_SELECTOR,"li>ul>li:nth-child(3)")[1].click()#选择部门
        self.driver.find_elements(By.XPATH,'//*[@class="qui_btn ww_btn ww_btn_Blue"]')[1].click()

    def test_get_department_name(self):#断言
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)  # 浏览器复用
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.find_elements(By.CSS_SELECTOR, ".frame_nav_item_title")[1].click()
        sleep(5)
        #name_list = []
        # eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(1)")
        eles = self.driver.find_elements(By.CSS_SELECTOR, 'li[role="treeitem"]')
        print("--->", len(eles))
        print(eles[2].text)
        assert "CBA_TEST" in eles[3].get_attribute('title').strip()
        # for ele in eles:
        #     name_list.append(ele.get_attribute("title"))
        # return name_list