import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_qw_addressbook():
    otp=webdriver.ChromeOptions()
    otp.debugger_address="127.0.0.1:8888"
    driver=webdriver.Chrome(options=otp)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
    driver.find_element(By.XPATH,'//*[@class="frame_nav"]/a[2]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@class="ww_operationBar"]/a[1]').click()
    elements=driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
    for ele in elements:
        if ele.get_attribute("title")=="东邪":
            return True
        print(ele.text)