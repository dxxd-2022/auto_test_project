import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_remote():#一般在登录场景中依赖扫码时，可以使用复用浏览器绕过扫码操作，复用浏览器也可以直接让我们运行指定操作
    # （复用中，拿到cookie，调试中很实用）
    otp=webdriver.ChromeOptions()
    otp.debugger_address="127.0.0.1:8888"
    driver=webdriver.Chrome(options=otp)#以上配置是设置driver
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
    driver.find_element(By.XPATH,"//*[@class='frame_nav']/a[2]").click()
    cookies=driver.get_cookies()
    with open("./cookies.yaml",'w',encoding='utf-8') as f:
        yaml.dump(cookies,f)#通过序列化把cookie写入yaml文件
    # print(cookies)
    driver.quit()
def test_cookie():#依赖扫码登录时，可以采用获取cookie的方式
    #打开新的浏览器，设置cookie,跳过扫码登录
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    #方式一：通过上面获取到的cookie信息，直接赋值
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_we')
    cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850418157803'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324983464287'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850418157803'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'jXme2v-AhFFencfgKfx4sxyoHlnNhX89ZvDfX355oCJCPTr487cWmHejsHWv0uP1pPRYsiLy3OdMcQjwUGeAZndR6oOsH_hZNt1grb17Zb0_SEai7XcuqDsnEQJ4xqLr44zjTdCIp4OVi8fBsjJgk8x2Z70fZfsa9NbNwjmxQ3X7BUi0L2i1P7ujmZe46og3hmLdzeMzJVhSYufZRogsVjXf0E5qnJZdEtFaVpCMi7GTiot9Pr0gX5uI7C71zSIJMn7TwEhVKBbZHxuL7Jx_FA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'hkQhVcfBTaIiznJmz8UNJZcu3PJ0TvyJP_Hkx7jr0FQCxGQyGkxZLGG_gJBD8VfO'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '28184039532244657'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.qq.com', 'expiry': 1638700690, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.378164445.1638599066'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '5326586272'}, {'domain': '.work.weixin.qq.com', 'expiry': 1669470746, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1637934690'}, {'domain': '.work.weixin.qq.com', 'expiry': 1641206821, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8528015'}, {'domain': '.qq.com', 'expiry': 2147483651, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '8032d2cc719d2ef5adcb9c86261a273fc9a67c4118fc5bfd92f90b6f42c02991'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': '6BI16mhuSf'}, {'domain': '.qq.com', 'expiry': 1701686290, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2042076379.1624885647'}, {'domain': '.work.weixin.qq.com', 'expiry': 1656421196, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#profile")
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="profile_navigation"]//li[2]').click()
    time.sleep(10)
    driver.quit()
def test_cookie_file():
    #从cookies文件中获取cookie信息
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu')
    with open("./cookies.yaml",encoding='utf-8')as f:#反序列化取出cookie
        cookie_data=yaml.safe_load(f)
    for cookie in cookie_data:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#profile")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="profile_navigation"]//li[2]').click()
    time.sleep(10)