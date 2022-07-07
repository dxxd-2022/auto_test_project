import time

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLogin:
    def setup_class(self):
        opt = Options()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def test_get_cookies(self):
        cookies=self.driver.get_cookies()
        with open("./qw_cookies",mode='w',encoding="utf-8")as f:
            yaml.safe_dump(cookies,f)
    def test_add_contact(self):
        with open("./qw_cookies")as f:
            cookies_data=yaml.safe_load(f)
        for cookie in cookies_data:
            self.driver.add_cookie(cookie)
        self.driver.find_elements(By.CSS_SELECTOR, ".frame_nav_item_title")[2].click()

