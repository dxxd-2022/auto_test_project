
import yaml
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_remote():#通过复用浏览器绕开扫码登录，方便于脚本调试
    opt = Options()
    opt.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=opt)
    driver.find_element(By.XPATH,'//*[@id="menu_cooperation"]').click()
    cookies=driver.get_cookies()
    with open("./cookie_datas.yaml","w",encoding='utf-8')as f:#把获取到的cookies信息保存到文件中
        yaml.safe_dump(cookies,f)
def test_cookie():#通过cookie的方式实现登录
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    with open("./cookie_datas.yaml",encoding='utf-8')as f:#通过从获取到的cookies文件中取出cookie信息，再设置cookie
        cookies=yaml.safe_load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
