import pytest
import allure
@allure.feature('搜索模块')
@allure.severity(allure.severity_level.NORMAL)#指定用例级别
class TestSearch:
    @allure.story('搜索成功')
    def test_search_success(self):
        print('搜索成功')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('搜索失败')
    def test_search_failure(self):
        print('搜索失败')


@allure.feature('登录模块')
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:
    @allure.story('登录成功')
    def test_login_success(self):
        with allure.step("进入登录页面"):
            print('登录页面')
        with allure.step("输入正确的用户名和密码"):
            print("用户名密码输入完成")
        with allure.step("点击登录按钮"):
            print("点击登录")
        print("登录成功")

    @allure.story('登录失败')
    def test_login_failure(self):
        with allure.step('输入错误的用户名'):
            print('输入错误的用户名')
        with allure.step('输入正确的密码'):
            print('输入正确的密码')
        with allure.step('点击登录'):
            assert "登录失败"=="登录失败"
            print('登录失败')
if __name__ == '__main__':
    pytest.main()