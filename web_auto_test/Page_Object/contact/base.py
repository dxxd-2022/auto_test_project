from selenium import webdriver


class Base:
    #初始化driver的封装，加if主要是解决类继承时造成的重复初始化问题
    def __init__(self,driver_base:webdriver=None):
        if driver_base is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(3)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self.driver=driver_base
    #以下是对find相关方法的封装
    def find(self,location,element):
        ele=self.driver.find_element(location,element)
        return ele
    def finds(self,location,elements):
        eles=self.driver.find_elements(location,elements)
        return eles
    def find_and_click(self,location,element):
        ele=self.driver.find_element(location,element)
        ele.click()