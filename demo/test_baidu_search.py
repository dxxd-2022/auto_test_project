import allure
from selenium import webdriver
import time
import pytest
@allure.testcase("https://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_datas',['allure','pytest','python'])
def test_step_demo(test_datas):
    with allure.step("打开百度网页"):
        dri=webdriver.Chrome()
        dri.get("https://www.baidu.com")
        dri.maximize_window()
    with allure.step(f"输入搜索词:{test_datas}]"):
        dri.find_element_by_id("kw").send_keys(test_datas)
        time.sleep(2)
        dri.find_element_by_id("su").click()
        time.sleep(2)
    with allure.step("保存图片"):
        dri.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        dri.quit()